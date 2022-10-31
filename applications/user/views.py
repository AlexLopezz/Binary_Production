from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import ( UserSerializer, RegisterSerializer,
                          CustomSerializer, RegisterAdminSerializer,ModifySerializer, ReservaUserSerializer)
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework.decorators import api_view
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from .models import User
from django.db.models import Q

# Register API
class RegisterAPI(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
        if self.request.data['role'] == 1:
            serializer_class = RegisterAdminSerializer
        else:
            serializer_class = RegisterSerializer

        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user, context=self.get_serializer_context()).data, status= status.HTTP_200_OK)

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response (UserSerializer(user).data,status= status.HTTP_200_OK)
        else:
            return Response("Datos erroneos. Username y/o contraseña erroneas.",status = status.HTTP_400_BAD_REQUEST)

#METODOS GET - APLICACION DE USUARIOS

@api_view(['GET'])
def allUserDB(request):
    if request.method == 'GET':

        all_user = User.objects.all() #Obtendre todos los usuarios registrados en la base de datos.
        if all_user:
            serializer = CustomSerializer(all_user, many=True) #Serializo mi lista de objetos(en este caso) a JSON para retornar en el GET.
            return Response(serializer.data)
        else:
            return Response("No existen usuarios registrados actualmente", status = status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def filterMitre(request):
    if request.method == 'GET':
        mitre = User.objects.filter(
            role__name="Maitre")
        if mitre:
            serializer =CustomSerializer(mitre, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No existen usuarios en el ROL de MITRE.", status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def filterMozo(request):
    if request.method == 'GET':
        mozo = User.objects.filter(
            role__name="Mozo")
        if mozo:
            serializer =CustomSerializer(mozo, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response("No existen usuarios en el ROL de MOZO.", status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def filterCaja(request):
    if request.method == 'GET':
        caja = User.objects.filter(
            role__name="Caja")
        if caja:
            serializer =CustomSerializer(caja, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No existen usuarios en el ROL de CAJA.", status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def filterClient(request):
    if request.method == 'GET':
        userClient = User.objects.filter(
            role__name="Usuario")
    if userClient:
        serializer= CustomSerializer(userClient, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    else:
        return Response("No existen usuarios en el ROL de USUARIO")


# METODO DELETE:
@api_view(['DELETE'])
def deleteUser(request):
    if request.method == 'DELETE':
        user_id = request.query_params.get('id')
        user= User.objects.get(pk = user_id)
        if user:
            user.delete()
            return Response("Se elimino correctamente el usuario",status=status.HTTP_200_OK)
        else:
            return Response("Usuario con ese ID, no encontrado.", status=status.HTTP_400_BAD_REQUEST)

#METODO PUT:
@api_view(['PUT'])
def modifyUser(request):
    if request.method == 'PUT':
        user_to_modify = User.objects.get(pk=request.data['id'])
        serializer =  ModifySerializer(user_to_modify, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(f"Hubo un problema: {serializer.erros}", status=status.HTPP_400_BAD_REQUEST)

@api_view(['GET'])
def filterForUser(request):
    if request.method == 'GET':
        user = User.objects.filter(
            Q(username__icontains = request.query_params.get('username')) |
            Q(fullname__icontains = request.query_params.get('username')) |
            Q(role__name ="Usuario")).distinct()

        if user:
            serializer = ReservaUserSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No se encontro usuario con ese nombre.")

@api_view(['GET'])
def myUser(request):
    if request.method == 'GET':
        user = User.objects.get(pk=request.query_params['id'])
        if user:
            serializer = CustomSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def filterForUsername(request):
     if request.method == 'GET':
        user = User.objects.filter(
            Q(username__icontains = request.query_params.get('username'))).distinct()

        if user:
            serializer = CustomSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No se encontro usuario con ese nombre.")