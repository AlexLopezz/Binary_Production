from rest_framework import serializers
from .models import Product, Menu, Category
from drf_extra_fields.fields import Base64ImageField

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

        
class ProductSerializer(serializers.ModelSerializer):
    img = Base64ImageField(required=False)
    class Meta:
        model = Product
        fields = (
                  'id',
                  'name',
                  'description',
                  'price',
                  'img',
                  )

class MenuSerializerGET(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Menu
        fields = (
            'name',
            'products',
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
