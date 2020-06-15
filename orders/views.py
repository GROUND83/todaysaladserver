
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Order
from .serializers import OrderSerializer
from .permissions import IsSelf

from django.conf import settings
# from django_filters.rest_framework import DjangoFilterBackend


class OrdersViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    allowedIps = ['129.0.0.1', '127.0.0.1']

    def get_permissions(self):
        print(self.action)
        if self.action == "list":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]



    @action(detail=False, methods=["post"])
    def importcallback(self, request):
        user_ip = request.META['REMOTE_ADDR']
        
        # imp_uid = request.data.get("imp_uid")
        # merchant_uid = request.data.get("merchant_uid")
        # status = request.data.get("status")
        print(settings.ALLOWED_HOSTS)
        for ip in settings.ALLOWED_HOSTS:
            if ip == user_ip:
                # 오더 크리에이트
                # 결재정보조회
                return Response('Ip Access!')

            else:
                return Response('Invalid Ip Access!')
    # @action(detail=False, methods=["get"])     
    # def createorder(self, request):
    #     importRes = self.importhook()
    #     access_token = importRes["access_token"]
    #     now = importRes["now"]
    #     expired_at = importRes["expired_at"]
    #     print(access_token)
    #     return Response( )