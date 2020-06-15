from django.db import models
from cores import models as core_models


class Event(core_models.TimeStampedModel):
    class Meta:
        verbose_name = "이벤트"
        verbose_name_plural = "이벤트"

    name = models.CharField(
        max_length=140, null=True, verbose_name="이벤트제목", unique=True
    )

    description = models.TextField(null=True, verbose_name="이벤트설명",)
    photo = models.ImageField(
        blank=True, upload_to="events_photos", help_text="700px300px"
    )
    detailphoto = models.ImageField(
        blank=True, upload_to="events_photos", help_text="700px1200px"
    )
    isActive = models.BooleanField(default=False, verbose_name="이벤트진행중",)

    def __str__(self):
        return self.name
