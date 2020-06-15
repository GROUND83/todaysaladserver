from django.db import models
from cores import models as core_models


class Order(core_models.TimeStampedModel):
    class Meta:
        verbose_name = "주문"
        verbose_name_plural = "주문"
        ordering = ["-created"]

    merchant_uid = models.CharField(
        max_length=30, null=False, blank=True, verbose_name="mid"
    )
    salad = models.ForeignKey(
        "salads.Salad",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="샐러드",
    )
    saladAmount = models.IntegerField(null=True, blank=True, verbose_name="샐러드수량",)
    fruit = models.ForeignKey(
        "fruitboxes.Fruitbox",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="과일박스",
    )
    fruitAmount = models.IntegerField(null=True, blank=True, verbose_name="과일박스수량",)
    # user = models.CharField(max_length=30, null=False, blank=True, verbose_name="유져")
    orderType = models.CharField(
        max_length=30, null=False, blank=True, verbose_name="오더타입"
    )
    deliveryDate = models.DateField(null=True, blank=True, verbose_name="배송일")
    user = models.CharField(max_length=30, null=False, blank=True, verbose_name="주문자")
    address = models.CharField(max_length=30, null=False, blank=True, verbose_name="주소")
    address1 = models.CharField(
        max_length=30, null=False, blank=True, verbose_name="주소1"
    )
    etc = models.CharField(max_length=30, null=False, blank=True, verbose_name="현관")
    tel = models.CharField(max_length=30, null=False, blank=True, verbose_name="전화번호")
    number = models.CharField(
        max_length=30, null=False, blank=True, verbose_name="오더횟수"
    )

    def __str__(self):
        if self.salad and self.fruit is not None:
            return "{} {} by {}".format(self.salad, self.fruit, self.user)
        elif self.salad is not None and self.fruit is None:
            return "{} by {}".format(self.salad.name, self.user)
        elif self.salad is None and self.fruit is not None:
            return "{} by {}".format(self.fruit.name, self.user)
