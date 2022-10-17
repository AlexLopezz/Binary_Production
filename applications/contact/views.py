from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
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
