from django.db import models
from applications.user.models import User

# Create your models here.
class Reservation(models.Model):
    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones - Restaurante Sentidos."
        
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    phone = models.CharField("Telefono celular", max_length=50)
    schedule = models.CharField("Horario", max_length=20)
    date = models.CharField("Fecha de Reservacion", max_length=50)
    selected_tables = models.CharField("Mesas seleccionadas", max_length=80) #Seleccion de mesas.
    paid_parcial = models.BooleanField("Pagado Parcial", default=False)
    paid = models.BooleanField("Pagado Total", default=False)


    def __str__(self):
        return f"Reserva de {self.user_id.username}"
