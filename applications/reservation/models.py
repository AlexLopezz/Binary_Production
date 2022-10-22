from django.db import models
from applications.user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Tables(models.Model):
    number_mesa=models.PositiveBigIntegerField(verbose_name="Mesa",validators=[MinValueValidator(1), MaxValueValidator(20)])
    is_selected= models.BooleanField(verbose_name="Esta seleccionado", default=False)
    def __str__(self):
        return f"Mesa N°{self.number_mesa}"


class Reservation(models.Model):
    class Meta:
        verbose_name = "Reservacion"
        verbose_name_plural = "Reservaciones - Restaurante Sentidos."

    user_id = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name="Usuario")
    phone = models.CharField("Telefono celular", max_length=50)
    schedule = models.CharField("Horario", max_length=20)
    date = models.DateField(verbose_name="Fecha")
    selected_tables = models.ManyToManyField(Tables, blank=True)
    paid_parcial = models.BooleanField("Pagado Parcial", default=False)
    paid = models.BooleanField("Pagado Total", default=False)


    def __str__(self):
        return f"Reserva de {self.user_id.username}"

