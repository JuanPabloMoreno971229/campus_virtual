from django.contrib import admin
from .models import User

# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('ID','name', 'category')
    readonly_fields = ('created', 'updated')

admin.site.register(User, UsuariosAdmin)