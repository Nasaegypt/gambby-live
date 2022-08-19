from rest_framework.serializers import ModelSerializer, SerializerMethodField
from service.models import Service, Category, SubCategory
from cities_light.models import City, Region
from django.contrib.auth.models import User


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['name']


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = ['name', "latitude", "longitude"]


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ['name']


class OwnerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ServiceSerializer(ModelSerializer):
    category = CategorySerializer()
    sub_category = SubCategorySerializer()
    service_city = CitySerializer()
    service_region = RegionSerializer()
    owner = OwnerSerializer()
    image = SerializerMethodField()

    class Meta:
        model = Service
        fields = '__all__'

    def get_image(self, service):
        request = self.context.get('request')
        image = service.image.url
        return request.build_absolute_uri(image)
