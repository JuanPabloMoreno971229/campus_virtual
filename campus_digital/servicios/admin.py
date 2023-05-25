from .models import  Services
from django.contrib import admin

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    readonly_fields = ('created', 'updated')

admin.site.register(Services, ServicesAdmin)