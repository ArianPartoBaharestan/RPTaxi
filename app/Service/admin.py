from django.contrib import admin
from . import models


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'LogoImg')
    search_fields = ['name',]
admin.site.register(models.Service, ServiceAdmin)





