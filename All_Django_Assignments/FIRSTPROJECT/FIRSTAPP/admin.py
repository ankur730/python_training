from django.contrib import admin
from FIRSTAPP.models import Detail

# Register your models here.
# Creating Model based on Admin for Display purposes on Django Database
class DetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'contact', 'address']


admin.site.register(Detail, DetailAdmin)

