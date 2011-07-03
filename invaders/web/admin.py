from django.contrib.gis import admin
from web.models import InvaderLocation

admin.site.register(InvaderLocation) #, admin.GeoModelAdmin)