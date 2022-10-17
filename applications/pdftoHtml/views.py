from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, View
from applications.food.models import Food
from django.http import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template

class FoodPDFView(View):
    def get(self, request, *args, **kwargs):
        template = get_template('listPDF_Food.html')
        listFood = Food.objects.all()
        data= {
            'listFood' : listFood,
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