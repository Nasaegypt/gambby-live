from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from cities_light.models import City, Country, Region

# Create your models here.

SERVICE_TYPE = (
    ('At Home', 'At Home'),
    ('In Place', 'In Place'),
)
AVAILABILITY = (
    ('Active', 'Active'),
    ('Not Active', 'Not Active')
)
COST = (
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High')
)


def image_upload(instance, filename):
    imagename, extention = filename.split(".")
    return "services/%s.%s" % (instance.id, extention)


class Service(models.Model):  # table
    owner = models.ForeignKey(User, related_name='service_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)  # column
    # location
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=500)
    service_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    service_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    service_city = models.ForeignKey(City, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=15, choices=SERVICE_TYPE)
    cost = models.CharField(max_length=10, choices=COST)
    availability = models.CharField(max_length=10, choices=AVAILABILITY)
    image = models.ImageField(upload_to=image_upload, null=True, blank=True, default='services/logo2.png')
    published_at = models.DateTimeField(auto_now=True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(70, 70)], format='JPEG',
                                     options={'quality': 60})
    slug = AutoSlugField(populate_from='title', unique=True, allow_unicode=True, editable=True)

    def save(self, *args, **kwargs):
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
