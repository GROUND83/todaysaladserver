from django.contrib.auth.models import AbstractUser
from django.db import models
from cores import managers as core_managers


class User(AbstractUser):

    """ custom User model """

    class Meta:

        verbose_name_plural = "고객"

    GENDER_MALE = "male"
    GENDER_FAMALE = " female"
    GENDER_CHOICES = (
        (GENDER_MALE, "남성"),
        (GENDER_FAMALE, "여성"),
    )
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, verbose_name="성별"
    )
    # destination = models.ManyToManyField(
    #     "destinations.Destination",
    #     related_name="desitni",
    #     max_length=30,
    #     verbose_name="도착지",
    #     null=False,
    # )
    email = models.CharField(max_length=30, null=False, unique=True, verbose_name="이메일")
    phone = models.CharField(max_length=11, null=True, unique=True, verbose_name="전화번호")
    birthdate = models.DateField(null=True, verbose_name="생년월일")
    policy = models.BooleanField(default=False, verbose_name="개인정보처리방침")
    servicepolicy = models.BooleanField(default=False, verbose_name="서비스이용약관")
    objects = core_managers.CustomUserManager()
    # favorites = models.ManyToManyField(
    #     "favorites.Favorite", related_name="favorites", blank=True
    # )

    def __str__(self):
        return self.first_name
