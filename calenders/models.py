from django.db import models
from cores import models as core_models
from salads.models import Salad
from fruitboxes.models import Fruitbox
from easyfoods.models import EasyFood


class Calender(core_models.TimeStampedModel):

    day = models.DateField(
        "일자", help_text="샐러드 일자를 입력하세요.", unique=True, null=True, blank=True
    )
    salad = models.ForeignKey(
        Salad, on_delete=models.CASCADE, blank=True, null=True, verbose_name="샐러드선택"
    )
    fruit = models.ForeignKey(
        Fruitbox, on_delete=models.CASCADE, blank=True, null=True, verbose_name="과일박스"
    )
    easyfood = models.ForeignKey(
        EasyFood, on_delete=models.CASCADE, blank=True, null=True, verbose_name="간편식"
    )
    isHoliday = models.BooleanField("공휴일여부", help_text="자동계산 입력하지 마세요.", default=True)
    holiday = models.CharField("공휴일", max_length=30, null=True, blank=True)
    month = models.CharField(
        "월", max_length=100, null=True, blank=True, help_text="자동계산 입력하지 마세요."
    )
    year = models.CharField(
        "년", max_length=100, null=True, blank=True, help_text="자동계산 입력하지 마세요."
    )
    date = models.CharField(
        "일", max_length=100, null=True, blank=True, help_text="자동계산 입력하지 마세요."
    )
    dayofweek = models.CharField(
        "요일", max_length=100, null=True, blank=True, help_text="자동계산 입력하지 마세요."
    )

    def __str__(self):
        return f"{self.salad}-{self.day}"

    def save(self, *args, **kwargs):
        if self.day:
            self.month = self.day.strftime("%m")
            self.year = self.day.strftime("%y")
            self.date = self.day.strftime("%d")
            self.dayofweek = self.day.strftime("%A")
            print(self.holiday)
            if self.holiday is not None:
                self.isHoliday = True
            elif self.holiday is None:
                self.isHoliday = False
            super(Event, self).save(*args, **kwargs)

    class Meta:

        verbose_name = "샐러드달력"
        verbose_name_plural = "샐러드달력"
        ordering = ["day"]
