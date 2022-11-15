# Create your views here.
from django.views.generic import View, DetailView
from applications.product.models import Product
from django.http import HttpResponse
from xhtml2pdf import pisa
from applications.checking_in.models import Invoice
from django.template.loader import get_template


class FoodPDFView(View):
    def get(self, request, *args, **kwargs):
        template = get_template('listPDF_Food.html')
        ProductFood = Product.objects.filter(category__name="Sentidos")
        data= {
            'ProductFood' : ProductFood,
        }
        html = template.render(data)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Comidas.pdf"'
        pisaStatus = pisa.CreatePDF(
            html, dest=response
        )

        if pisaStatus.err:
            return HttpResponse("Hubo errores.")
        else:
            return response

class InvoiceDetail(DetailView):
    model = Invoice
    template_name = "invoice.html"

class InvoiceViewPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        invoice = Invoice.objects.get(number_invoice=request.GET.get('id'))
        data= {
            'invoice' : invoice,
        }
        html = template.render(data)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Factura.pdf"'
        pisaStatus = pisa.CreatePDF(
            html, dest=response
        )

        if pisaStatus.err:
            return HttpResponse("Hubo errores.")
        else:
            return response