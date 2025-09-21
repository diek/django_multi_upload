# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import IncidentImage, IncidentReport, IncidentImages


from django.utils.html import mark_safe


@admin.register(IncidentImage)
class IncidentImageAdmin(admin.ModelAdmin):
    list_display = ("id", "thumbnail", "uploaded_at")
    list_filter = ("uploaded_at",)

    def thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return ""

    thumbnail.short_description = "Image"


@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "date_reported", "show_images")
    list_filter = ("date_reported",)

    def show_images(self, obj):
        images = obj.images.all()
        html = ""
        for image in images:
            html += f'<img src="{image.image.url}" width="50" style="margin:2px;" />'
        return mark_safe(html)

    show_images.short_description = "Images"


@admin.register(IncidentImages)
class IncidentImagesAdmin(admin.ModelAdmin):
    list_display = ("id", "incident_report", "incident_image")
    list_filter = ("incident_report", "incident_image")
