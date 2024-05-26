from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "year", "make", "IMEI", "body_style", "license", "status", "image")
    list_filter = ("status", "body_style", "license")
    search_fields = ("model", "make", "IMEI", "year")


admin.site.register(Car, CarAdmin)
