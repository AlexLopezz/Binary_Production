from django.db import models
from applications.user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class OpinionsUser(models.Model):
    class Meta:
        verbose_name = "Opiniones acerca del Restaurante Sentidos"
        verbose_name_plural = "Opiniones acerca del Restaurante Sentidos"

    user = models.ForeignKey(User,on_delete=models.PROTECT, max_length=150)
    comment = models.CharField("Comentario", max_length=50)
    attention = models.IntegerField("Atencion", validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    place = models.IntegerField("Lugar", validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    food = models.IntegerField("Comida", validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    price = models.IntegerField("Precio", validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)

    def __str__(self):
        return self.user.username