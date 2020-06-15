from django.contrib import admin
from . import models
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin


@admin.register(models.Postcode)
class PostcodeAdmin(ImportExportMixin, admin.ModelAdmin):
    pass
