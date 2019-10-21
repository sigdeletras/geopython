

from django.contrib.gis.db import models

class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    localizacion = models.PointField()
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)


from django.contrib.gis.admin import OSMGeoAdmin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(OSMGeoAdmin):
    list_display = ('nombre', 'localizacion')