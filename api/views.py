from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ServiceSerializer
from service.models import Service


@api_view(['GET'])
def getServices(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True, context={"request": request})
    return Response(serializer.data)


@api_view(['GET'])
def getServicesBySubCategory(request, subcategory):
    services = Service.objects.all()
    filtered = services.filter(sub_category__name__iexact=subcategory)
    serializer = ServiceSerializer(filtered, many=True, context={"request": request})
    return Response(serializer.data)
