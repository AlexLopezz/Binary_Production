from django.urls import path
from .views import (FoodSentidos, ProductList,ProductDetailView, 
ShowImageField, filterForCategory, menuAdmin, filterForNameMenu, allCategories,
filterForNameProduct, filterForNameAndCategoryProduct, filterNameProductExactly)

app_name = 'product'

urlpatterns = [
    path('api/products/', ProductList.as_view()),
    path('description/<food_slug>/',ProductDetailView.as_view()),
    path('imgJson/', ShowImageField.as_view(), name= 'IMGJson'),
    path('api/FoodSentidos/', FoodSentidos.as_view()),
    path('api/filterName/', filterNameProductExactly),
    path('api/filterNameProduct/', filterForNameProduct),
    path('api/filterProductAndCategory/', filterForNameAndCategoryProduct),
    path('api/filterCategory/', filterForCategory),
    path('api/menuAdmin/', menuAdmin), #Retorna todos los menus, con sus respectivos productos.
                                       #Para hacer el post: name(string), products[id(products)....]
    path('api/filterMenu/', filterForNameMenu),
    path('api/allCategories/', allCategories),
    
]

