from django.db import models
from cores import models as core_models


class Fruitbox(core_models.TimeStampedModel):
    class Meta:
        verbose_name = "과일박스"
        verbose_name_plural = "과일박스"

    # month = models.DateField(null=True, blank=True, verbose_name="과일박스 달")
    name = models.CharField(max_length=140, null=True, verbose_name="과일박스", unique=True)
    description = models.TextField(null=True, verbose_name="과일박스설명", blank=True)
    ingredients = models.ManyToManyField(
        "ingredients.Ingredient",
        related_name="fruitBox",
        blank=True,
        verbose_name="재료",
    )
    photo = models.ImageField(blank=True, upload_to="fruitbox_photos")

    def __str__(self):
        return self.name
