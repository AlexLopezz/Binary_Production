from django.db import models
# Create your models here

class Category(models.Model):
    class Meta:
        verbose_name= "Categoria de Productos - Restaurante Sentidos y Casa de Te."
        verbose_name_plural= "Categorias de Productos - Restaurante Sentidos y Casa de Te."
        ordering = ('name',)
    
    name = models.CharField(verbose_name="Nombre", max_length= 20)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name= models.CharField(verbose_name="Nombre producto", max_length=80, unique=True)
    description= models.TextField(verbose_name= "Descripcion", max_length=80, blank=True, null=True, default="Sin descripcion...")
    price = models.FloatField(verbose_name="Precio", null=False, blank=False)
    img= models.ImageField(verbose_name="Imagen representativa", null=True, blank=True)
    published= models.DateField("Fecha de publicacion", auto_now_add=True)
    category = models.ManyToManyField(Category, verbose_name="Categoria",blank=True) 

    class Meta:
        verbose_name= "Producto - Restaurante Sentidos"
        verbose_name_plural = "Productos - Restaurante Sentidos"
        ordering = ('-name',)
    
    def __str__(self):
        return self.name


class Menu(models.Model):
    class Meta:
        verbose_name= "Menu - Restaurante Sentidos & Casa de Te"

    name = models.CharField(verbose_name="Nombre del menu", max_length=50)
    products = models.ManyToManyField(Product, blank=True, verbose_name="Productos del menu")

    def __str__(self) -> str:
        return self.name    
