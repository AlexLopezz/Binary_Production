from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import ( UserSerializer, RegisterSerializer,
                          CustomSerializer, RoleSerializer,ModifySerializer)
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework.decorators import api_view
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from .models import User

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
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
            role__name="Mitre")
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

# METODO DELETE:
@api_view(['DELETE'])
def deleteUser(request):
    if request.method == 'DELETE':
        try:
            user_id = request.query_params.get('id')
            user= User.objects.get(pk = user_id)
            if user:
                user.delete()
                return Response("Se elimino correctamente el usuario",status=status.HTTP_200_OK)
        except:
            return Response("No se encontro usuario con ese ID.",status = status.HTTP_400_BAD_REQUEST)

#METODO PUT:
@api_view(['PUT'])
def modifyUser(request):
    if request.method == 'PUT':
        user_to_modify = User.objects.get(pk=request.data['id'])
        serializer =  ModifySerializer(user_to_modify, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Se modifico usuario, correctamente.", status= status.HTTP_200_OK)
        else:
            return Response(f"Hubo un problema: {serializer.erros}", status=status.HTPP_400_BAD_REQUEST)