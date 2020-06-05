from django.contrib import admin
from blog_posts.models import Contacts

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']

admin.site.register(Contacts, ContactAdmin)
