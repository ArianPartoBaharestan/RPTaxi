from django.db import models
from Service.models import Service


class TransferRequest(models.Model):
    user = models.ForeignKey(Service, on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.user)