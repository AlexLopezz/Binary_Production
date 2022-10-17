from .models import Reservation
from rest_framework import serializers
from applications.user.serializers import UserSerializer

class MyReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'id',
            'schedule',
            'date',
            'paid',
            'paid_parcial',
            'selected_tables')

class ReservationSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Reservation
        fields = '__all__'

class Selected_Table_Serializer(serializers.ModelSerializer):# Serializa las mesas seleccionadas.
    class Meta:
        model = Reservation
        fields = (
            'selected_tables',
        )

class PaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'id',
            'paid',
            'paid_parcial'
        )