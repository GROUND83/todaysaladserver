from django.contrib import admin
from . import models
from django.utils.html import mark_safe
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from import_export import resources


@admin.register(models.SaladType)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Salad)
class SaladAdmin(ImportExportMixin, admin.ModelAdmin):
    # inlines = (PhotoInline,)
    fieldsets = (
        ("기본정보", {"fields": ("name", "description", "salad_type",)},),
        ("재료", {"fields": ("ingredients",)}),
        (
            "추가정보",
            {
                "fields": (
                    "calory",
                    "price",
                    "unit",
                    "amount",
                    "totalsugars",
                    "totalfat",
                    "totalcarbohydrate",
                    "totalprotein",
                    "totalcholesterol",
                    "totalsalt",
                    "totalpotassium",
                    "totaldietaryfiber",
                    "photo",
                )
            },
        ),
        ("주문가능", {"fields": ("instant_order",)}),
    )
    list_display = ("name", "price", "calory", "unit", "instant_order")

    list_filter = (
        "instant_order",
        "salad_type",
    )
    search_fields = ("=name", "^host__username")
    filter_horizontal = ("ingredients", "salad_type")

    def count_calory(self, obj):
        return obj.ingredients.count()

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            super().save_model(request, obj, form, change)
        else:
            pass

    def save_related(self, request, form, formsets, change):
        form.save_m2m()
        for formset in formsets:
            self.save_formset(request, form, formset, change=change)
        super().save_model(request, form.instance, form, change)


# @admin.register(models.Photo)
# class PhotoAdmin(admin.ModelAdmin):

#     list_display = ("__str__", "get_thumbnail")
#     # list_filter = "get_type"

#     def get_thumbnail(self, obj):
#         return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

#     # def get_type(self, obj):
#     #     return obj.ingredient.ingredient_type

#     get_thumbnail.short_description = "Thumbnail"
