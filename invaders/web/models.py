from django.contrib.gis.db import models

# Create your models here.
class InvaderLocation(models.Model):
    name = models.CharField(max_length=100)
    descriptipn = models.TextField(null=True, blank=True)
    point = models.PointField()
    image_url = models.CharField(max_length=256)
