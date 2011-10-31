from django.contrib.gis import admin
from web.models import Location

admin.site.register(Location) #, admin.GeoModelAdmin)