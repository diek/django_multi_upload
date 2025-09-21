# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import IncidentImage, IncidentReport, IncidentImages


@admin.register(IncidentImage)
class IncidentImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at')
    list_filter = ('uploaded_at',)


@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date_reported')
    list_filter = ('date_reported',)
    raw_id_fields = ('images',)


@admin.register(IncidentImages)
class IncidentImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'incident_report', 'incident_image')
    list_filter = ('incident_report', 'incident_image')
