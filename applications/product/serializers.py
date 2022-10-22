from rest_framework import serializers
from .models import Product
from drf_extra_fields.fields import Base64ImageField


class ProductSerializer(serializers.ModelSerializer):
    img = Base64ImageField(required=False)
    class Meta:
        model = Product
        fields = (
                  'name',
                  'description',
                  'price',
                  'img',
                  )

