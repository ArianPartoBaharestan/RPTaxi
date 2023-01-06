from django.contrib import admin
from . import models


class TransferRequestAdmin(admin.ModelAdmin):
    list_display = ('status', 'user', 'driver', 'service', 'total_price', 'created_on')
    search_fields = ['user', 'driver']
    list_filter = ("created_on", "service", "driver", "user", "status")
admin.site.register(models.TransferRequest, TransferRequestAdmin)





