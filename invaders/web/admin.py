from django.contrib.gis import admin
from models import Location

admin.site.register(Location) #, admin.GeoModelAdmin)
