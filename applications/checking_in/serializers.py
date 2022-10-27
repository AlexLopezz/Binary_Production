from rest_framework import serializers
from applications.user.serializers import InvoiceUSerSerializer
from .models import Invoice, Order, ProductOrder



class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = (
            'product',
            'quantity',
            'price',
        )

#Serializer para metodo GET. Mostrar todos los pedidos.
class OrderSerializer(serializers.ModelSerializer):
    products = ProductOrderSerializer(many=True, source="productorder_set")

    class Meta:
        model = Order
        fields = (
                  'id',
                  'table',
                  'products',
                  )


#Serializer para POST - Realiza un pedido.
class OrderSerializerPOST(serializers.ModelSerializer):
    products = ProductOrderSerializer(many=True, source="productorder_set")

    class Meta:
        model = Order
        fields = (
                  'id',
                  'table',
                  'products',
                  )

    def create(self, validated_data):
        products_data = validated_data.pop('productorder_set')
        order = Order.objects.create(**validated_data)

        for p in products_data:
            ProductOrder.objects.create(**p, order=order)

        return order

#Serializador para mostrar las facturas.
class InvoiceSerializerGET(serializers.ModelSerializer):
    user = InvoiceUSerSerializer()
    order = OrderSerializer()
    class Meta:
        model = Invoice
        fields = (
            'number_invoice',
            'user',
            'date',
            'order',
        )

#Serializer para metodo POST - Crear una nueva factura.
class InvoiceSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            'user',
            'order',
        )