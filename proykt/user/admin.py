from django.contrib import admin
from .models import User

@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'bio')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
