from django.contrib import admin
from .models import Reservation
# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'usuario',
        'date',
        'schedule',
        'paid',
        'paid_parcial',
    )
    search_fields = (
        'user_id',
        'date',
        'schedule',
        )
    
    list_filter = (
        'user_id',
        'date',
        'schedule',
    )
    
    def usuario(self, obj):
        return obj.user_id.username

admin.site.register(Reservation, ReservationAdmin)