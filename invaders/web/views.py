from django.contrib.gis.geos import Point
from web.models import InvaderLocation
from layar import LayarView, POI
from django.contrib.gis.measure import D

default_unit = 'm'
class InvaderLayar(LayarView):
    # make sure to accept **kwargs
    def get_ljubljanainvaders_queryset(self, latitude, longitude, radius, **kwargs):
        print InvaderLocation.objects.filter(location__distance_lte=(Point(longitude, latitude), D(m=radius)))
        return InvaderLocation.objects.filter(location__distance_lte=(Point(longitude, latitude), D(m=radius)))

    def poi_from_ljubljanainvaders_item(self, item):
        return POI(id=item.id, lat=item.location.y, lon=item.location.x, title=item.name,
                    line2=item.description, line3='Distance: %distance%', image_url='http://188.230.158.192:8000'+item.image_url)

invader_layar = InvaderLayar()
