from django.urls import path
from .views import FoodSentidos, ProductList,ProductDetailView, ShowImageField, filterForCategory

app_name = 'product'

urlpatterns = [
    path('api/products/', ProductList.as_view()),
    path('description/<food_slug>/',ProductDetailView.as_view()),
    path('imgJson/', ShowImageField.as_view(), name= 'IMGJson'),
    path('api/FoodSentidos/', FoodSentidos.as_view()),
    path('api/filterCategory/', filterForCategory),
]

