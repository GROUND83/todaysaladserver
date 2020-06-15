
from django.contrib import admin
from . import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    # inlines = (PhotoInline,)
    fieldsets = (
        ("기본정보", {"fields": ("name", "description", "photo","detailphoto","isActive")},),
        
    )
    list_display = ("name", )

   


