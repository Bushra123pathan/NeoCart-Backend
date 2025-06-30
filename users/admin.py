from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'role', 'is_active', 'is_staff', 'created_at')
    list_filter = ('role', 'is_active')
    search_fields = ('email', 'username')
