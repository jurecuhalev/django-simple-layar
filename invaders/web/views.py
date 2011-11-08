from django.contrib.gis.geos import Point
from models import Location
from layar import LayarView, POI
from django.contrib.gis.measure import D

default_unit = 'm'
HOST = 'http://mfru.livecd.net'
class InvaderLayar(LayarView):
    # make sure to accept **kwargs
    def get_mfru_queryset(self, latitude, longitude, radius, **kwargs):
        print Location.objects.filter(location__distance_lte=(Point(longitude, latitude), D(m=radius)))
        return Location.objects.filter(location__distance_lte=(Point(longitude, latitude), D(m=radius)))

    def poi_from_mfru_item(self, item):
        return POI(id=item.id, lat=item.location.y, lon=item.location.x, title=item.name,
                    line2=item.description, line3='Distance: %distance%', image_url=HOST+item.image.url)

invader_layar = InvaderLayar()
