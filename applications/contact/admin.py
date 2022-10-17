from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'read',
        'fullname',
        'email',
        'phone',
        'date_contact',
    )
    search_fields = ('fullname', 'email', 'phone')
    list_filter = ('fullname', 'email', 'phone')

admin.site.register(Contact, ContactAdmin)