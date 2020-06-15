from django.db import models
from cores import models as core_models
from users.models import User


class Destination(core_models.TimeStampedModel):

    address = models.CharField(max_length=140, null=True, verbose_name="주소")
    room = models.CharField(max_length=140, null=True, verbose_name="호수")
    zonecode = models.CharField(max_length=140, null=True, verbose_name="우편번호")
    etc = models.CharField(max_length=200, null=True, verbose_name="추가사항")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="도착지", null=True
    )

    def __str__(self):
        return self.address
