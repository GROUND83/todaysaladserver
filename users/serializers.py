from rest_framework import serializers
from .models import User

from destinations.serializiers import DestinationSerializer


class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "phone",
            "policy",
            "servicepolicy",
        )
        read_only_fields = ("id",)

    # 계정생성
    def create(self, validated_data):
        print("벨리데이터", validated_data)
        # password = validated_data.get("password")
        user = super().create(validated_data)
        user.set_unusable_password()
        user.save()
        return user
