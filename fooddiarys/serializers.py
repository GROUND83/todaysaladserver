from rest_framework import serializers
from .models import Fooddiary


class FooddiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Fooddiary
        exclude = ("created", "updated")
