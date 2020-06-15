from django.contrib import admin
from . import models


@admin.register(models.Destination)
class DestinationAdmin(admin.ModelAdmin):
    fieldsets = (
        ("기본정보", {"fields": ("address", "user", "zonecode", "room", "etc",)},),
    )
    list_display = ("address",)
