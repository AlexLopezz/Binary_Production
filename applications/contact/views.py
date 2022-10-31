from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Contact
from .serializers import ContactSerializer
# Create your views here.
class ContactAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Todo salio bien",
                "Datos enviados": serializer.data,
            },status = status.HTTP_200_OK)
        else:
            return Response({
                "message": "Ocurrio un error.",
                "error": serializer.errors,
            }, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def allContact(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deleteAllContact(request):
    contacts = Contact.objects.all()
    for c in contacts:
        c.delete()
    return Response("Se eliminaron todas las consultas.", status = status.HTTP_200_OK)

@api_view(['GET'])
def deleteContact(request):
    contact = Contact.objects.get(fullname=request.query_params.get('fullname'))
    if contact:
        contact.delete()
        return Response("Contacto eliminado", status= status.HTTP_200_OK)
    else:
        return Response("No se encontro contacto.", status = status.HTTP_400_BAD_REQUEST)
