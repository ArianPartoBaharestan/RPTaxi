from django.db import models
from Service.models import Service
from authentication.models import User


class TransferRequest(models.Model):
    STATUS_CHOICES = (('searching_for_driver', 'در جستجو راننده'),
                      ('waiting_for_driver', 'در انتظار راننده'),
                      ('driver_arrived', 'راننده به مبدا رسیده'),
                      ('passenger_boarded', 'مسافر سوار شده'),
                      ('on_the_way_to_destination', 'در مسیر به مقصد'),
                      ('arrived_at_destination', 'به مقصد رسیده'),
                      ('cancelled', 'سفر لغو شده'))
    PAYMENT_CHOICES = (('in_cash', 'نقدی'), ('online', 'آنلاین'))
    status = models.CharField(max_length=256, choices=STATUS_CHOICES, default='searching_for_driver')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver', null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    origin_location = models.CharField(max_length=256)
    destination_location = models.CharField(max_length=256)
    total_price = models.IntegerField(default=0)
    payment_method = models.CharField(max_length=256, choices=PAYMENT_CHOICES, default='in_cash')
    paid = models.BooleanField(default=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + str(self.status)