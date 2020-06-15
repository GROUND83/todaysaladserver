from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Calender
from .serializers import CalenderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters


class CalendersViewSet(ModelViewSet):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    # 퍼미션 설정
    filter_backends = [
        DjangoFilterBackend,
    ]
    filter_fields = ("year", "month", "date")

    def get_permissions(self):

        print(self.action)
        if self.action == "create":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]


class CalenderMonthViewSet(ModelViewSet):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    # 퍼미션 설정
    filter_backends = [
        filters.DjangoFilterBackend,
    ]

    filter_fields = ("year", "month")

    def get_permissions(self):

        print(self.action)
        if self.action == "create":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    @action(detail=False)
    def search(self, request):
        start_date = request.GET.get("start_date", None)
        end_date = request.GET.get("end_date", None)
        print(start_date, end_date)
        # start_date = datetime.date(2005, 1, 1)
        # end_date = datetime.date(2005, 3, 31)
        calender = Calender.objects.filter(day__range=[start_date, end_date])
        serializer = CalenderSerializer(calender, many=True)
        return Response(serializer.data)
