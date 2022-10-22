from .models import Reservation
from .models import Tables
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer



class Selected_Table_Serializer(serializers.ModelSerializer):# Serializa las mesas seleccionadas
    class Meta:
        model = Tables
        fields = (
            'id',
            'number_mesa',
        )

class getReservationSerializer(serializers.ModelSerializer): #Sera utilizado para las solicitudes GET, generalmente para mostrar todas las reservas o una en particular.
    user_id = serializers.StringRelatedField()
    selected_tables = Selected_Table_Serializer(many=True)
    class Meta:
        model = Reservation
        fields = (
            'id',
            'user_id',
            'phone',
            'schedule',
            'date',
            'paid',
            'paid_parcial',
            'selected_tables')

class  getTableReservationSerializer(serializers.ModelSerializer):
    selected_tables = Selected_Table_Serializer(many=True)
    class Meta:
        model = Reservation
        fields = ('selected_tables',)

class ReservationSerializer(serializers.ModelSerializer): #SERIALIZER POST : Sera utilizado para serializar el request POST, para registrar reservaciones.

    class Meta:
        model = Reservation
        fields = ['user_id', 'phone', 'schedule', 'date', 'selected_tables']


class PaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'id',
            'paid',
            'paid_parcial'
        )

