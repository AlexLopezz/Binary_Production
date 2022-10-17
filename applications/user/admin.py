from django.contrib import admin
from .models import User, Role
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'fullname',
        'dni',
        'Admin',
        'id'
    )
    search_fields = (
        'role.name',
        'email',
        'fullname'
    )
    list_filter = (
        'role',
        'email',
    )
    
    def Admin(self, obj):
        return obj.is_staff

class RoleAdmin(admin.ModelAdmin):
    list_display= (
        'name',
        'description',
        'id'
        )

    search_fields= (
        'name',
    )
admin.site.register(User, UserAdmin)

admin.site.register(Role, RoleAdmin)
    