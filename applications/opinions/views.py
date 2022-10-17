import math
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status

from applications.reservation.models import Reservation
from .serializers import OpinionsUserSerializers, ListUserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import OpinionsUser


# Create your views here.
class OpinionsUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = OpinionsUserSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "Opinion": serializer.data,
            },status = status.HTTP_200_OK)
        else:
            return Response({
                "message": serializer.errors,
            }, status = status.HTTP_400_BAD_REQUEST)


class ListOpinion(APIView):

    def get(self, request, *args, **kwargs):
        opinions_list = OpinionsUser.objects.all()

        serializerOpinions = ListUserSerializer(opinions_list,many=True)
        return Response(serializerOpinions.data)

@api_view(['GET'])
def getAverage(request):
    if request.method == 'GET':
        try:
            allOpinions = OpinionsUser.objects.all()
            attention = 0
            place = 0
            food = 0
            price = 0
            lengthOpinions = len(allOpinions)

            for contact in allOpinions:
                attention += contact.attention
                place += contact.place
                food += contact.food
                price += contact.price

            #Promedio:
            averageAttention = attention / lengthOpinions
            averagePlace = place / lengthOpinions
            averageFood = food / lengthOpinions
            averagePrice = price /lengthOpinions

            return Response({
                "Message": "Promedio de Puntuaciones",
                "Atencion": math.trunc(averageAttention),
                "Lugar": math.trunc(averagePlace),
                "Comida": math.trunc(averageFood),
                "Precio": math.trunc(averagePrice)
            },status = status.HTTP_200_OK)

        except:
            return Response({
                "Message": "No existen opiniones, por lo que no podemos hacer un promedio de todas ellas."
            },status= status.HTTP_400_BAD_REQUEST)
