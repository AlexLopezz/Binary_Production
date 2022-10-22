from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

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
            imgShow = Product(**validated_data)
            imgShow.save()

            serializer_response = ProductSerializer(imgShow)

            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    