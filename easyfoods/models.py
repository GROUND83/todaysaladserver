from django.db import models
from cores import models as core_models


class EasyFood(core_models.TimeStampedModel):
    class Meta:
        verbose_name = "간편식"
        verbose_name_plural = "간편식"

    name = models.CharField(max_length=140, null=True, verbose_name="간편식", unique=True)
    description = models.TextField(null=True, verbose_name="간편식설명", blank=True)
    ingredients = models.ManyToManyField(
        "ingredients.Ingredient",
        related_name="easyfood",
        blank=True,
        verbose_name="재료",
    )
    photo = models.ImageField(blank=True, upload_to="easyfood_photos")

    def __str__(self):
        return self.name
