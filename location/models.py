from django.contrib.gis.db import models
# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
