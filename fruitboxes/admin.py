from django.contrib import admin
from . import models


@admin.register(models.Fruitbox)
class FruitboxAdmin(admin.ModelAdmin):

    fieldsets = (
        ("기본정보", {"fields": ("name", "description", "photo")},),
        ("재료", {"fields": ("ingredients",)}),
    )
    list_display = ("name",)
    filter_horizontal = ("ingredients",)
