from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Fruitbox
from .serializers import FruitboxSerializer


class ListFruitboxView(ListAPIView):

    queryset = Fruitbox.objects.all()
    serializer_class = FruitboxSerializer
    # filter_backends = [
    #     DjangoFilterBackend,
    # ]
    # filter_fields = ("ingredient_type",)


class SeeFruitboxView(RetrieveAPIView):

    queryset = Fruitbox.objects.all()
    serializer_class = FruitboxSerializer
