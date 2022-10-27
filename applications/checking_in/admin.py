from django.contrib import admin
from .models import Invoice, Order, ProductOrder, Method_Pay
# Register your models here.
class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductOrderInline,]



admin.site.register(Order, OrderAdmin)
admin.site.register(Invoice)
admin.site.register(Method_Pay)