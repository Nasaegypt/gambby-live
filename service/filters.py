import django_filters
from .models import Service


class ServiceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Service
        fields = '__all__'
        exclude = ['owner', 'published_at', 'image', 'image_thumbnail', 'slug', 'service_city']
