from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Invoice, Order
from .serializers import (InvoiceSerializerGET, InvoiceSerializerPOST,OrderSerializer,
OrderSerializerPOST, PaySerializerPUT)



@api_view(['GET',])
def orderGET(request):
    if request.method == 'GET':
        order= Order.objects.filter(pay= False) #Filtraremos todos los pedidos que no esteen pagados/no posean una factura.
        #Si la lista es mayor a 0, significa que el filtro contiene objetos de tipo Order.
        if len(order) > 0:
            serializer = OrderSerializer(order, many=True) #Serializamos la lista obtenida.
            return Response(serializer.data, status= status.HTTP_200_OK) #Enviamos un status 200, con los pedidos encontrados.
        else:
            return Response("No se encontraron pedidos actualmente.", status=status.HTTP_404_NOT_FOUND) #Si no lo encuentra, enviamos un STATUS 404.

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

@api_view(['PUT'])
def updatePaidOrder(request):
    if request.method == 'PUT':
        order = Order.objects.get(pk = request.query_params.get('id'))
        serializer = PaySerializerPUT(order, data = request.data)
        if serializer.is_valid():
            order.pay = request.query_params.get('pay')
            order.save()
            return Response("Update", status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def filterInvoice(request):
    if request.method == 'GET':
        dateStart = request.query_params.get('dateStart') #Fecha de inicio.
        dateEnd = request.query_params.get('dateEnd') #Fecha de fin.
        method_pay = request.query_params.get('method_pay') #Metodo de pago elegido.
        #la variable invoices sera una lista, donde contendremos todos aquellos objetos que cumplan con el filtro:
        invoices = Invoice.objects.filter(
            date__range=(dateStart, dateEnd), #Le damos un rango de fechas: Donde le pasamos la fecha de inicio(dateStart) y una fecha final(dateEnd).
            method_pay__name = method_pay #Ademas de ello, le pasamos el metodo de pago, en este caso podremos mandar el nombre del metodo.
        )
        if len(invoices) > 0: #Verificamos la longitud de la lista: Si es  mayor a 0, significa que tenemos una lista con objetos Invoices.
            serializer = InvoiceSerializerGET(invoices, many=True) #Serializamos la lista.
            return Response(serializer.data, status= status.HTTP_200_OK) #Enviamos a traves del Response.(STATUS 200)
        else:
            return Response("No se encontraron resultados en ese rango de fechas.", status=status.HTTP_404_NOT_FOUND) #De lo contrario, enviamos un mensaje con status 404 NOT FOUND.