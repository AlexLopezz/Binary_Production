from django.contrib import admin
from .models import OpinionsUser
# Register your models here.

class OpinionAdmin(admin.ModelAdmin):
    list_display= (
        'id',
        'usuario',
        'comment',
        'attention',
        'place',
        'food',
        'price',
    )
    def usuario(self,obj):
        return obj.user
    
    list_filter = ('user',)

    
admin.site.register(OpinionsUser, OpinionAdmin)