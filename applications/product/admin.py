from django.contrib import admin
from .models import Product, Category
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'description',
        'id',
    )

    list_filter = (
        'category',
        'name',
    )
    
    search_fields = (
        'category',
        'name',
    )
    
    filter_horizontal= ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)