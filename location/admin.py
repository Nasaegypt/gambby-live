from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Location
# Register your models here.


@admin.register(Location)
class LocationAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')