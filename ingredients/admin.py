from django.contrib import admin
from . import models
from django.utils.html import mark_safe
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin


@admin.register(models.Ingredient)
class IgredientAdmin(ImportExportMixin, admin.ModelAdmin):

    fieldsets = (
        ("기본정보", {"fields": ("ingredient_type", "name", "description",)},),
        (
            "추가정보",
            {
                "fields": (
                    "calory",
                    "baseunit",
                    "amount",
                    "baseprice",
                    "sugars",
                    "fat",
                    "carbohydrate",
                    "protein",
                    "cholesterol",
                    "salt",
                    "potassium",
                    "dietaryfiber",
                    "photo",
                )
            },
        ),
        (
            "계산된 정보",
            {
                "fields": (
                    "weightForCalory",
                    "weightForSugars",
                    "weightForFat",
                    "weightForCarbohydrate",
                    "weightForProtein",
                    "weightForCholesterol",
                    "weightForSalt",
                    "weightForPotassium",
                    "weightForDietaryfiber",
                )
            },
        ),
        ("주문가능", {"fields": ("instant_order",)}),
    )

    list_display = (
        "name",
        "weightForCalory",
        "calory",
        "baseprice",
        "baseunit",
        "amount",
        "instant_order",
        "ingredient_type",
    )
    list_filter = (
        "instant_order",
        "ingredient_type",
    )

    search_fields = ("=name", "^host__username")
