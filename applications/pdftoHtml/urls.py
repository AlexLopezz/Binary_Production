from django.urls import path
from .views import FoodPDFView

urlpatterns = [
    path('listtoPDF/', FoodPDFView.as_view()),
]