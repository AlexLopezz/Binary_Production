from django.urls import path
from .views import FoodPDFView,InvoiceViewPDF, InvoiceDetail



urlpatterns = [
    path('listtoPDF/', FoodPDFView.as_view()),
    path('viewPDF/<pk>/', InvoiceDetail.as_view()),
    path('api/PDFInvoice/', InvoiceViewPDF.as_view()), #Para generar la factura, se debe pasar el ID de la factura por parametro.(?id:number_invoice)

]   