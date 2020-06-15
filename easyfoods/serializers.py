from rest_framework import serializers
from .models import EasyFood


class EasyFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = EasyFood
        exclude = ("created", "updated")
