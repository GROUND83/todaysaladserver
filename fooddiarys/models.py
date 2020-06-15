from django.db import models
from cores import models as core_models


class Fooddiary(core_models.TimeStampedModel):
    class Meta:
        verbose_name = "음식일기"
        verbose_name_plural = "음식일기"

    name = models.CharField(
        max_length=140, null=True, verbose_name="음식일기명", unique=True
    )
    caption = models.CharField(max_length=200, verbose_name="내용")
    date = models.DateField(null=True, verbose_name="일자")
    author = models.ForeignKey(
        "users.User", related_name="users", on_delete=models.CASCADE, null=True
    )


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    class Meta:
        verbose_name = "음식일기사진"
        verbose_name_plural = "음식일기사진"

    caption = models.CharField(max_length=80, verbose_name="사진이름")
    file = models.ImageField(upload_to="fooddiary_photos")
    salad = models.ForeignKey(
        Fooddiary, related_name="photos", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.caption
