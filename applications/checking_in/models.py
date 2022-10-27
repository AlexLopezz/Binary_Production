from django.db import models
from applications.product.models import Product
from applications.reservation.models import Tables
from applications.user.models import User
# Create your models here.
class Order(models.Model):
    table = models.ForeignKey(Tables, on_delete=models.CASCADE,verbose_name="Mesa")
    products = models.ManyToManyField(Product, through="ProductOrder", verbose_name="Productos", blank=True)
    
    def __str__(self) -> str:
        return f"Pedido N°{self.id}"
    
    class Meta:
        verbose_name="Pedidos - Restaurante Sentidos y Casa de Te"
        
    

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE, verbose_name="Producto")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Pedido", blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Cantidad")
    price = models.FloatField(verbose_name="Precio", default=1)
    
    def __str__(self) -> str:
        return f"Productos elegidos"
    
class Invoice(models.Model):
    number_invoice= models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    date = models.DateField(auto_now_add=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"Factura N°{self.number_invoice}"
    
    class Meta:
        verbose_name="Facturas - Restaurante Sentidos y Casa de Te"
    