from django.contrib.gis.db import models

# Create your models here.
class InvaderLocation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    location = models.PointField()
    image_url = models.CharField(max_length=256)

    objects = models.GeoManager()

    def __unicode__(self): return self.name