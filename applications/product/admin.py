from django.contrib import admin
from .models import Menu, Product, Category
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

class MenuAdmin(admin.ModelAdmin):
    list_display= ('name','id',)

    filter_horizontal = ('products',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Menu, MenuAdmin)
