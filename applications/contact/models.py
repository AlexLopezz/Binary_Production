from django.db import models

# Create your models here.
class Contact(models.Model):
    read= models.BooleanField("Leido", default=False)
    fullname = models.CharField("Nombre completo", max_length=80)
    email = models.EmailField("Email",max_length=120)
    message = models.CharField("Mensaje", max_length=50)
    phone = models.CharField("Telefono", max_length=20)
    date_contact = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Consulta de contacto - Restaurante Sentidos"
        verbose_name_plural = "Consultas de contacto - Restaurante Sentidos"

    def __str__(self):
        return f"Consulta de: {self.fullname}"