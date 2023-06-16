from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Commissions_USF)
class Commissions_USFAdmin(admin.ModelAdmin):
    list_display = ("id_category","id_subcategory","name_commission")
    search_fields = ("name_commission",)
    list_filter = ("name_commission",)
    ordering = ("id_category",)

@admin.register(models.Input_Commissions_USF)

class Input_Commissions_USF(admin.ModelAdmin):
    list_display = ("idfk_commission","date_of_entry")
    search_fields = ("idfk_commission",)
    list_filter = ("idfk_commission",)
    ordering = ("idfk_commission",)

@admin.register(models.Discount_CommissionsBank_USF)
class Discount_CommissionsBank_USF(admin.ModelAdmin):
    list_display = ("name_client","idfk_commission","percent_discount")
    search_fields = ("idfk_commission",)
    list_filter = ("idfk_commission",)
    ordering = ("name_client",)
