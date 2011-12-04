from django.contrib.gis import admin
from models import Location, Category

class LocationAdmin(admin.ModelAdmin):
	list_display=('name', 'location', 'image', 'url')


admin.site.register(Location, LocationAdmin) #, admin.GeoModelAdmin)
admin.site.register(Category)