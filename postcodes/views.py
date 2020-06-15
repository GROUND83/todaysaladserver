
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Postcode
from .serializers import PostcodeSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ListPostcodeView(ListAPIView):

    queryset = Postcode.objects.all()
    serializer_class = PostcodeSerializer
    filter_backends = (DjangoFilterBackend,) 
    filter_fields = ('postcode', )

   