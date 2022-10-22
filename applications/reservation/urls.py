from django.urls import path
from .views import (ReservationAPIView, MyReservationAPIView,
deleteReservationAPIView, detailReservationAPIView, getTableSelectedAPIView, allReservationAPIView, filterForDateReservation,
paidReservationAPIView, filterForDateReservation)

app_name = 'reservation'

urlpatterns = [
    path('api/reservation/', ReservationAPIView.as_view()), #POST - REGISTRA LAS RESERVAS
    path('api/getReservation/', getTableSelectedAPIView), #GET - RETORNA LAS MESAS SELECCIONADAS
    path('api/myReservation/', MyReservationAPIView.as_view()), #GET - RETORNA TODAS LAS RESERVACIONES DEL USER.
    path('api/deleteReservation/', deleteReservationAPIView), #DELETE - ELIMINA UNA RESERVACION CON ESE ID.
    path('api/detailReservation/', detailReservationAPIView ), #GET - ACTUALIZA LA RESERVA
    path('api/allReservation/', allReservationAPIView ), #GET - TODAS LAS RESERVAS.
    path('api/paidReservation/', paidReservationAPIView),
    path('api/filterForDate/', filterForDateReservation), #GET - ME DEBE ENVIAR EL PARAMETRO Y LE RETORNO TODAS LAS RESERVAS DE ESE DIA.
]