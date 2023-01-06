from django.db import models
from django.utils.html import format_html


class Service(models.Model):
    name = models.CharField(max_length=256, unique=True)
    logo = models.ImageField(upload_to='service/logo')
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def LogoImg(self):
        return format_html("<img width=30 src='{}'>".format(self.logo.url))

    def __str__(self):
        return str(self.name)