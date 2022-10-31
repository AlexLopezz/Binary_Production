from django.urls import path
from .views import detailOrder, orderGET, orderPOST, checking_in

app_name = 'checking_in'

urlpatterns = [
    path('api/allOrder/', orderGET),
    path('api/orderPost/', orderPOST),
    path('api/checking_invoice/', checking_in),
    path('api/detailOrder/', detailOrder)
]