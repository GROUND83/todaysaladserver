from django.contrib import admin
from . import models
from django.utils.html import mark_safe


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Fooddiary)
class FooddiaryAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    list_display = ("name",)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("__str__", "get_thumbnail")
    # list_filter = "get_type"

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    # def get_type(self, obj):
    #     return obj.ingredient.ingredient_type

    get_thumbnail.short_description = "Thumbnail"
