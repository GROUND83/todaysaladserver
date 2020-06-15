from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import EasyFood
from .serializers import EasyFoodSerializer


class ListEasyFoodView(ListAPIView):

    queryset = EasyFood.objects.all()
    serializer_class = EasyFoodSerializer
    # filter_backends = [
    #     DjangoFilterBackend,
    # ]
    # filter_fields = ("ingredient_type",)


class SeeEasyFoodView(RetrieveAPIView):

    queryset = EasyFood.objects.all()
    serializer_class = EasyFoodSerializer
