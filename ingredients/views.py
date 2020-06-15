from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Ingredient
from .serializers import IngredientSerializer


class ListIngredientView(ListAPIView):

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = ("ingredient_type",)


class SeeIngredientView(RetrieveAPIView):

    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
