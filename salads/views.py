
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Salad
from .serializers import SaladSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ListSaladsView(ListAPIView):

    queryset = Salad.objects.all()
    serializer_class = SaladSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = ("name",)


class SeeSaladView(RetrieveAPIView):

    queryset = Salad.objects.all()
    serializer_class = SaladSerializer
