from django.db import models
from cores import models as core_models
import openpyxl


class Postcode(models.Model):
    class Meta:
        verbose_name = "주문가능지역"
        verbose_name_plural = "주문가능지역"

    postcode = models.IntegerField(null=True, verbose_name="우편번호")

    def __str__(self):
        return str(self.postcode)
