import jwt
import os
import hashlib
import hmac
import json
import base64
import time
import requests
from random import randint
from django.conf import settings
from django.contrib.auth import login, logout
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from .my_auth import UserBackend

# from favorites.serializers import FavoriteSerializer
# from favorites.models import Favorite
from .models import User
from .serializers import UserSerializer
from destinations.serializiers import DestinationSerializer
from .permissions import IsSelf


def make_signature(string):
    SMS_SERVICE_SECRET = os.environ.get("SMS_SERVICE_SECRET")
    secret_key = bytes(SMS_SERVICE_SECRET, "UTF-8")
    string = bytes(string, "UTF-8")
    string_hmac = hmac.new(secret_key, string, digestmod=hashlib.sha256).digest()
    string_base64 = base64.b64encode(string_hmac).decode("UTF-8")
    return string_base64


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # 퍼미션 설정

    def get_permissions(self):
        # list 는 어드민 유저만
        print(self.action)
        if self.action == "list":
            permission_classes = [IsAdminUser]
        elif (
            self.action == "retrieve"
            or self.action == "favs"
            or self.action == "update"
            or self.action == "put"
        ):
            permission_classes = [IsSelf]
        else:
            # self.action == "create" or self.action == "login"
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    @action(detail=False, methods=["post"])
    def login(self, request):
        email = request.data.get("email")
        user = UserBackend.authenticate(self, request, email=email)
        if user is not None:
            print("로그인")
            print(user)
            encoded_jwt = jwt.encode(
                {"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256"
            )
            login(request, user, backend="users.my_auth.UserBackend")
            return Response({"token": encoded_jwt, "id": user.pk,})
        else:
            print("오류")
            return Response(
                data={"로그인 과정 중에 오류가 있습니다."}, status=status.HTTP_401_UNAUTHORIZED
            )

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)  # 유저를 pk로 가져온다
        except User.DoesNotExist:
            return None

    def put(self, request, pk):

        pk = request.data.get("pk", None)
        phone = request.data.get("phone", None)
        print(pk, phone)
        user = self.get_object()
        if pk is not None:
            try:
                user = User.objects.get(pk=pk)
                user.phone = phone
                user.save()
            except User.DoesNotExist:
                pass
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True)
    def destination(self, request):
        print("가져오기")
        user = self.get_object()
        print(user)
        serialzier = DestinationSerializer(user.destination.all(), many=True).data
        # serializer = FavoriteSerializer( many=True).data
        print(serialzier)
        return Response(serialzier)

    @action(detail=False, methods=["post"])
    def logout(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def sendsms(self, request):
        serviceId = os.environ.get("NAVER_SMS")
        SMS_ACCESS_KEY_ID = os.environ.get("SMS_ACCESS_KEY_ID")
        SMS_SEND_PHONE_NUMBER = os.environ.get("SEND_PHONE")
        phone_number = request.data.get("phone")
        print(phone_number)
        auth_number = randint(1000, 10000)
        timestamp = str(int(time.time() * 1000))
        url = "https://sens.apigw.ntruss.com"
        uri = "/sms/v2/services/" + serviceId + "/messages"
        api_url = url + uri
        string_to_sign = "POST " + uri + "\n" + timestamp + "\n" + SMS_ACCESS_KEY_ID
        signature = make_signature(string_to_sign)

        message = "안녕하세요? 투데이샐러드입니다. \n고객님의 인증번호는 [{}] 입니다.".format(auth_number)
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "x-ncp-apigw-timestamp": timestamp,
            "x-ncp-iam-access-key": SMS_ACCESS_KEY_ID,
            "x-ncp-apigw-signature-v2": signature,
        }
        body = {
            "type": "SMS",
            "contentType": "COMM",
            "countryCode": "82",
            "from": SMS_SEND_PHONE_NUMBER,
            "content": message,
            "messages": [{"to": phone_number}],
        }
        body = json.dumps(body)
        sms_requests = requests.post(api_url, headers=headers, data=body)
        sms_json = sms_requests.json()
        print(sms_json)
        if sms_json["statusCode"] == "202":
            return Response(auth_number, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def sendTrans(self, request):
        serviceId = os.environ.get("NAVER_SMS")
        SMS_ACCESS_KEY_ID = os.environ.get("SMS_ACCESS_KEY_ID")
        SMS_SEND_PHONE_NUMBER = os.environ.get("SEND_PHONE")
        phone_number = request.data.get("phone")
        totoalPrice = request.data.get("totalprice")
        print(phone_number)
        print(totoalPrice)
        timestamp = str(int(time.time() * 1000))

        url = "https://sens.apigw.ntruss.com"
        uri = "/sms/v2/services/" + serviceId + "/messages"
        api_url = url + uri
        string_to_sign = "POST " + uri + "\n" + timestamp + "\n" + SMS_ACCESS_KEY_ID
        signature = make_signature(string_to_sign)

        message = "안녕하세요? 투데이샐러드입니다.\n주문을 해주세서 감사합니다.\n결제계좌:[농협]: 302-6709-0956-01 김원창 \n결제금액을 [{}] 입금하시면 주문이 완료됩니다.\n항상 최선을 다하는 투데이샐러드가 되겠습니다.".format(
            totoalPrice
        )
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "x-ncp-apigw-timestamp": timestamp,
            "x-ncp-iam-access-key": SMS_ACCESS_KEY_ID,
            "x-ncp-apigw-signature-v2": signature,
        }
        body = {
            "type": "LMS",
            "contentType": "COMM",
            "countryCode": "82",
            "from": SMS_SEND_PHONE_NUMBER,
            "content": message,
            "messages": [{"to": phone_number}],
        }
        body = json.dumps(body)
        sms_requests = requests.post(api_url, headers=headers, data=body)
        sms_json = sms_requests.json()
        print(sms_json)
        if sms_json["statusCode"] == "202":
            return Response(status=status.HTTP_200_OK)

    # @action(detail=True)
    # def favs(self, request, pk):
    #     user = self.get_object()
    #     serializer = FavoriteSerializer(user.favorites.all(), many=True).data
    #     return Response(serializer)

    # @favs.mapping.put
    # def toggle_favs(self, request, pk):
    #     pk = request.data.get("pk", None)
    #     user = self.get_object()
    #     if pk is not None:
    #         try:
    #             favorite = Favorite.objects.get(pk=pk)
    #             if favorite in user.favorites.all():
    #                 user.favorites.remove(favorite)
    #             else:
    #                 user.favorites.add(favorite)
    #             return Response()
    #         except Favorite.DoesNotExist:
    #             pass
    #     return Response(status=status.HTTP_400_BAD_REQUEST)
