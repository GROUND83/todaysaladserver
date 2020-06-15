from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer


class ListEventView(ListAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = ("isActive",)


class SeeEventView(RetrieveAPIView):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
