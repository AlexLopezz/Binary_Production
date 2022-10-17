from requests import request
from yaml import serialize
from .models import Reservation
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import ListAPIView
from applications.user.models import User
from rest_framework.decorators import api_view
from applications.reservation.serializers import ReservationSerializer, MyReservationSerializer, Selected_Table_Serializer, PaidSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['PUT'])
def paidReservationAPIView(request):
    if request.method == 'PUT':
        reservation = Reservation.objects.get(pk=request.data['id'])

        serializer = PaidSerializer(reservation, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Se registro correctamente en la base de datos."
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "error": "Hubo un error."
            }, status = status.HTTP_400_BAD_REQUEST)


class ReservationAPIView(APIView): #ACTUALIZADO: Funciona para realizar las reservas.
    def post(self, request, *args, **kwargs):
        reservation = ReservationSerializer(data= request.data)
        if reservation.is_valid():
            reservation.save() #Registra en la DB, la registra y la manda a "data"
            return Response("Reserva guardada con exito", status = status.HTTP_200_OK)
        else:
            return Response(reservation.errors,status = status.HTTP_400_BAD_REQUEST)

class MyReservationAPIView(APIView): #Serializa solo las reservas de un usuario en particular, pasandole el ID del usuario.
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        myReservation = Reservation.objects.filter(user_id = user_id)
        serializer = MyReservationSerializer(myReservation, many=True)
        if myReservation:
            return Response(serializer.data)
        else:
            return Response({
                "message": "No se encontraron reservaciones",
            })

@api_view(['DELETE'])
def deleteReservationAPIView(request): #Elimina una reserva en particular, pasando el ID de la reserva.
    if request.method == 'DELETE':
        try:
            id_reservation = request.query_params.get('id')
            reservation = Reservation.objects.get(pk = id_reservation)
            if reservation:
                reservation.delete()
                return Response("Se elimino correctamente la reserva.", status=status.HTTP_200_OK)
        except:
            return Response("No se encontro reservacion con ese ID.",status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detailReservationAPIView(request): #Muestra en detalle una reserva, pasando el ID de la reserva.
    if request.method == 'GET':
        id = request.query_params.get('id')
        reservation = Reservation.objects.get(pk = id)
        serializer = MyReservationSerializer(reservation)
        return Response(serializer.data)

@api_view(['GET'])
def allReservationAPIView(request): #Muestra todas las reservas disponibles, o que esteen en la base de datos registradas.
    if request.method == 'GET':
        allReservation = Reservation.objects.all()
        serializer = MyReservationSerializer(allReservation, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No hay reservaciones registradas.", status=status.HTTP_404_NOT_FOUND)

class GetTableSelectedAPIView(ListAPIView): #Obtiene las reservas, mediante la fecha y horario que recibimos por GET.
    serializer_class = Selected_Table_Serializer
    def get_queryset(self):
        date = self.request.query_params.get('date')
        schedule = self.request.query_params.get('schedule')
        getReservation = Reservation.objects.filter(date=date, schedule=schedule)

        return getReservation

@api_view(['GET'])
def filterForDateReservation(request): #Obtiene todas las reservas de una determinada fecha, mediante el parametro que recibimos por GET.
    if request.method == 'GET':
        reservationDay = Reservation.objects.filter(date=request.query_params.get('date'))
        serializer =  MyReservationSerializer(reservationDay, many=True)
        return Response(serializer.data)



