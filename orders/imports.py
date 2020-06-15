from django.contrib.auth import get_user_model
import os
import json
import requests
from iamport import Iamport
from rest_framework.response import Response
from rest_framework import status

Order = get_user_model()


class Import(object):
    def get_permissin(self):
        imp_key = os.environ.get("IMPORT_REST_API")
        imp_secret = os.environ.get("IMPORT_REST_API_SECRET")
        # print(imp_key, imp_secret)
        api_url = "https://api.iamport.kr/users/getToken"
        headers = {
            "Content-Type": "application/json",
        }
        body = {"imp_key": imp_key, "imp_secret": imp_secret}
        body = json.dumps(body)
        getToken = requests.post(api_url, headers=headers, data=body)
        getToken_json = getToken.json()

        if getToken_json["code"] == 0:

            return getToken_json["response"]
        else:
            return False

    def get_payment(merchant_uid):
        merchant_uid = merchant_uid

        imp_key = os.environ.get("IMPORT_REST_API")
        imp_secret = os.environ.get("IMPORT_REST_API_SECRET")

        iamport = Iamport(imp_key=imp_key, imp_secret=imp_secret)
        response = iamport.find(merchant_uid=merchant_uid)

        print(response)
        return response
        # api_url = "https://api.iamport.kr/payment/" + imp_uid
        # headers = {
        #     "Content-Type": "application/json; charset=UTF-8",
        #     "Authorization": "timestamp",
        # }
        # sms_requests = requests.post(api_url, headers=headers)
        # sms_json = sms_requests.json()
        # print(sms_json)
        # if sms_json["statusCode"] == "202":
        #     return Response(auth_number, status=status.HTTP_200_OK)
