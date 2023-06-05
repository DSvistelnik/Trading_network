from django.contrib import admin
from authentication.models import User


class UserAdmin(admin.ModelAdmin):
    """Пользователь в панели администратора"""
    list_display = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_active', 'is_superuser']
    search_fields = ['username', 'email', 'first_name', 'last_name']


admin.site.register(User, UserAdmin)

