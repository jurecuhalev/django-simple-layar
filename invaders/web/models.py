from django.contrib.gis.db import models

class Category(models.Model):
	name = models.CharField(max_length=100)
	poi_id = models.IntegerField(blank=True, null=True)

	def __unicode__(self): 
		return "%s (%s)" % (self.name, self.poi_id)

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    location = models.PointField()
    image = models.ImageField(upload_to="uploads", max_length=256, null=True, blank=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    
    category = models.ForeignKey(Category, blank=True, null=True)
    objects = models.GeoManager()

    def __unicode__(self): return self.name