from rest_framework import serializers
from .models import Calender
from salads.serializers import SaladSerializer
from fruitboxes.serializers import FruitboxSerializer
from easyfoods.serializers import EasyFoodSerializer


class CalenderSerializer(serializers.ModelSerializer):
    salad = SaladSerializer()
    fruit = FruitboxSerializer()
    easyfood = EasyFoodSerializer()

    class Meta:
        model = Calender
        exclude = ("created", "updated")
