from django.urls import path
from .views import ContactAPIView

urlpatterns = [
    path('api/contact/', ContactAPIView.as_view())
]