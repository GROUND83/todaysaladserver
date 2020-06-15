from rest_framework import serializers
from .models import Order
from .imports import Import
from rest_framework.response import Response
from rest_framework import status


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ("created", "updated")
