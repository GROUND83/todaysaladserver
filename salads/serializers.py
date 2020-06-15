from rest_framework import serializers
from ingredients.serializers import IngredientSerializer
from .models import Salad


class SaladSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    photo = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Salad
        exclude = ("created", "updated")


class SaladNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salad
        fields = ["name", "id", "photo", "calory", "unit"]
