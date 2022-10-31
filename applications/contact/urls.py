from django.urls import path
from .views import ContactAPIView, allContact, deleteAllContact, deleteContact

urlpatterns = [
    path('api/contact/', ContactAPIView.as_view()),
    path('api/listContact/', allContact),
    path('api/deleteContact/', deleteContact),
    path('api/deleteAllContacts/', deleteAllContact),
]