from rest_framework import serializers
from .models import Fruitbox


class FruitboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruitbox
        exclude = ("created", "updated")
