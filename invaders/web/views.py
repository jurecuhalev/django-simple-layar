from django.contrib.gis.geos import Point
from models import Location
from layar import LayarView, POI
from django.contrib.gis.measure import D
from django.conf import settings
import random

default_unit = 'm'
HOST = settings.HOST

class InvaderLayar(LayarView):
    items = [1.0, 1.2, 1.5, 2.0, 2.3, 2.5, 2.8, 3.0, 3.3, 3.5, 3.8, 4.0]

    # make sure to accept **kwargs
    def get_mfru_queryset(self, latitude, longitude, radius, **kwargs):
        return Location.objects.filter(location__distance_lte=(Point(longitude, latitude), D(m=radius)))

    def poi_from_mfru_item(self, item):
        relative_alt = round(random.uniform(1, 6), 1)

        return POI(id=item.id, lat=item.location.y, lon=item.location.x, relative_alt=random.choice(self.items),
                    title=item.name,
                    line2=item.description, line3='Distance: %distance%', 
                    image_url=HOST+item.image.url, actions=[{'label':'Opis dogodka', 'uri':item.url}])

invader_layar = InvaderLayar()
