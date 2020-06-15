from rest_framework import serializers
from .models import Destination


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        exclude = ("created", "updated")

    def create(self, validated_data):
        print("주소생성")
        request = self.context.get("request")
        print(request)
        destination = Destination.objects.create(**validated_data, user=request.user)
        return destination
