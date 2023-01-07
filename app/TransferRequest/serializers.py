from rest_framework import serializers
from .models import TransferRequest


class TransferReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferRequest
        fields = '__all__'