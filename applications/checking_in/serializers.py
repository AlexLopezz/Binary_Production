from rest_framework import serializers
from .models import Invoice, Method_Pay, Order, ProductOrder

class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Method_Pay
        fields = '__all__'

class ProductOrderSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = (
            'product',
            'quantity',
            'price',
        )

class ProductOrderSerializerGET(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = ProductOrder
        fields = (
            'product',
            'quantity',
            'price',
        )

#Serializer para metodo GET. Mostrar todos los pedidos.
class OrderSerializer(serializers.ModelSerializer):
    products = ProductOrderSerializerGET(many=True, source="productorder_set")

    class Meta:
        model = Order
        fields = (
                  'id',
                  'table',
                  'products',
                  )


#Serializer para POST - Realiza un pedido.
class OrderSerializerPOST(serializers.ModelSerializer):
    products = ProductOrderSerializerPOST(many=True, source="productorder_set")

    class Meta:
        model = Order
        fields = (
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
    order = OrderSerializer()
    method_pay = serializers.StringRelatedField()
    class Meta:
        model = Invoice
        fields = (
            'number_invoice',
            'date',
            'order',
            'method_pay',
            'totalPrice',
        )

#Serializer para metodo POST - Crear una nueva factura.
class InvoiceSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            'number_invoice',
            'order',
            'method_pay',
            'totalPrice',
        )

class PaySerializerPUT(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'pay',
            )


