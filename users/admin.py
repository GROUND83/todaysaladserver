from django.contrib import admin
from . import models
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from import_export import resources

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(ImportExportMixin, admin.ModelAdmin):
    """ Custom User Admin """

    list_display = (
        "username",
        "first_name",
        "phone",
        "email",
    )
    list_filter = ("is_staff", "is_superuser")

    def __str__(self):
        return self.phone
