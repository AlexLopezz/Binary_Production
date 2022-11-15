from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Menu, Category
from .serializers import ProductSerializer, MenuSerializer, MenuSerializerGET, CategorySerializer, CategorySerializerPUT, ProductSerializerGET

# Create your views here.
class ProductList(APIView):
    def get(self, *args, **kwargs):
        list_Food = Product.objects.all()

        serializerFood = ProductSerializer(list_Food,many=True)
        return Response(serializerFood.data)

class ProductDetailView(APIView):
    def get(self, food_slug , *args, **kwargs):
        food = get_object_or_404(Product, slug= food_slug)
        serializer = ProductSerializer(food)
        return Response(serializer.data)

class FoodSentidos(APIView):
    def get(self, *args, **kwargs):
        foodSentidos = Product.objects.filter(category__name="Sentidos")
        if foodSentidos:
            serializer = ProductSerializer(foodSentidos, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response("No hay comidas en esta categoria", status= status.HTTP_404_NOT_FOUND)


@api_view(['GET',])
def filterForCategory(request):
    if request.method == 'GET':
        productCategory= Product.objects.filter(category__name= request.query_params['nameCategory'])
        if productCategory:
            serializer= ProductSerializer(productCategory, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def filterForCategoryExactly(request):
    if request.method == 'GET':
        productCategory= Product.objects.get(category__name= request.query_params['nameCategory'])
        if productCategory:
            serializer= ProductSerializer(productCategory, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ShowImageField(APIView):
    def get(self, request, *args):
        print(str(self.parser_classes))
        return Response({'parsers':' '.join(map(str,self.parser_classes))}, status = 204)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            archivo = validated_data['img']
            archivo.name = 'mi_foto.jpg'
            validated_data['img'] = archivo
            # Convertir y guardar el modelo
            product = Product.objects.create(
                name= validated_data['name'],
                description = validated_data['description'],
                price = validated_data['price'],
                img = validated_data['img']
            )
            product.category.set(validated_data['category'])

            serializer_response = ProductSerializer(product)

            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        product = Product.objects.get(pk=request.query_params.get('id'))

        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        product = Product.objects.get(name=request.query_params.get('nameProduct'))
        if product:
            product.delete()
            return Response("Se elimino correctamente.", status=status.HTTP_200_OK)
        else:
            return Response("No se encontro el producto con es ID.", status= status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def menuAdmin(request):
    if request.method == 'GET':
        menu = Menu.objects.all()
        serializer = MenuSerializerGET(menu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Success", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        menu = Menu.objects.get(pk=request.query_params.get('id'))
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Modify successfuly", status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        menu = Menu.objects.get(name=request.query_params.get('nameMenu'))
        if menu:
            menu.delete()
            return Response("Delete success", status=status.HTTP_200_OK)
        else:
            return Response("Error", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def filterForNameMenu(request):
    menu= Menu.objects.get(name=request.query_params.get('name'))
    if menu:
        serializer = MenuSerializerGET(menu)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def filterNameProductExactly(request):
    product= Product.objects.get(name=request.query_params.get('nameProduct'))
    if product:
        serializer = ProductSerializerGET(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def allCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def filterForNameProduct(request):
    if request.method == 'GET':
        product = Product.objects.filter(
            Q(name__icontains = request.query_params.get('nameProduct'))).distinct()

        if product:
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No se encontro usuario con ese nombre.")


@api_view(['GET'])
def filterForNameAndCategoryProduct(request):
    if request.method == 'GET':
        product = Product.objects.filter(
            Q(name__icontains = request.query_params.get('nameProduct')) &
            Q(category__name= request.query_params.get('nameCategory'))).distinct()

        if product:
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("No se encontro usuario con ese nombre.", status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def filterForCategoryName(request):
    if request.method == 'GET':
        category = Category.objects.get(name=request.query_params.get('nameCategory'))

        if category:
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
@api_view(['PUT'])
def modifyCategory(request):
    if request.method == 'PUT':
        category = Category.objects.get(pk = request.query_params.get('id'))

        if category:
            serializer = CategorySerializerPUT(category, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Modificado con exito.", status=status.HTTP_200_OK)
            else:
                return Response("Error.", status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteCategory(request):
    if request.method == 'DELETE':
        category = Category.objects.get(name = request.query_params.get('nameCategory'))
        if category:
            category.delete()
            return Response("Eliminado exitosamente.", status= status.HTTP_200_OK)
        else:
            return Response("No se encontro la categoria solicitada.", status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def postCategory(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Categoria creada correctamente.", status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)