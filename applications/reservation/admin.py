from django.contrib import admin
from .models import Reservation, Tables
# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'date',
        'schedule',
        'paid',
        'paid_parcial',
        'id',
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
    filter_horizontal= ('selected_tables',)

    def usuario(self, obj):
        return obj.user_id.username

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Tables)