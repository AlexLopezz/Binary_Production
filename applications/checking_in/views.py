from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Invoice, Order
from .serializers import InvoiceSerializerGET, InvoiceSerializerPOST,OrderSerializer, OrderSerializerPOST



@api_view(['GET',])
def orderGET(request):
    if request.method == 'GET':
        orderAll= Order.objects.all()
        serializer = OrderSerializer(orderAll, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

@api_view(['POST',])
def orderPOST(request):
    if request.method == 'POST':
        serializer = OrderSerializerPOST(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def checking_in(request):
    #Muestra todas las facturas disponibles/creadas en la BD.
    if request.method == 'GET':
        allInvoices = Invoice.objects.all() #Traigo todas las facturas
        serializer = InvoiceSerializerGET(allInvoices, many=True) #Las serializo a JSON, *many= True* indica que sera una lista de JSON que voy a enviar.

        return Response(serializer.data, status= status.HTTP_200_OK) #Envio un status 200, que todo salio bien y la lista JSON.

    #Realiza una factura si es POST.
    if request.method == 'POST':
        serializer = InvoiceSerializerPOST(data = request.data) #Serializo los datos del JSON (request.data).
        if serializer.is_valid(): #Verifico si la informacion cumple y es valida para guardar en la BD.
            serializer.save() #Si lo es, guardo en la Base de datos.
            return Response("Factura realizada con exito.", status = status.HTTP_200_OK) #Status 200, indicando que todo salio bien.
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST) #Nos dara status 400 si algun parametro no fue enviado correctamente.

@api_view(['GET'])
def detailOrder(request):
    if request.method == 'GET':
        order = Order.objects.get(pk=request.query_params.get('id'))
        if order:
            serializer = OrderSerializer(order)
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


