
import requests
from random import randint
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Fooddiary
from .serializers import FooddiarySerializer
from .permissions import IsSelf


class FooddiaryViewSet(ModelViewSet):
    queryset = Fooddiary.objects.all()
    serializer_class = FooddiarySerializer
    # 퍼미션 설정

    def get_permissions(self):
        # list 는 어드민 유저만
        if self.action == "create":
            print(self.action)
            permission_classes = [AllowAny]
        elif self.action == "list":
            print(self.action)
            permission_classes = [IsSelf]
           
        else:
            print(self.action)
            permission_classes = [IsSelf]
        return [permission() for permission in permission_classes]

    