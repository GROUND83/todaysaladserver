from django.contrib import admin
from . import models
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from import_export import resources


class EnrolmentResource(resources.ModelResource):
    class Meta:
        model = models.Order
        fields = (
            "merchant_uid",
            "salad",
            "saladAmount",
            "fruit",
            "fruitAmount",
            "orderType",
            "deliveryDate",
            "user",
            "address",
            "address1",
            "etc",
            "tel",
            "number",
        )

        widgets = {
            "deliveryDate": {"format": "%Y/%m/%d"},
        }


@admin.register(models.Order)
class OrderAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = EnrolmentResource
    list_display = (
        "__str__",
        "user",
        "number",
        "merchant_uid",
        "orderType",
        "deliveryDate",
    )
    list_filter = ("deliveryDate", "orderType")
