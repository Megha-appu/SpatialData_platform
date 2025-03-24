from django.shortcuts import render
from rest_framework import viewsets
from .models import PointLocation, PopulationDensity
from .serializers import MultipointLocationSerializer, PopulationDensitySerializer

# Viewset for Locations (Points)
# modelviewset performs all CRUD operations on api
class LocationViewSet(viewsets.ModelViewSet):
    queryset = PointLocation.objects.all()
    serializer_class = MultipointLocationSerializer

# Viewset for Population Density Areas (Polygons)
# modelviewset performs all CRUD operations on api
class DensityViewSet(viewsets.ModelViewSet):
    queryset = PopulationDensity.objects.all()
    serializer_class = PopulationDensitySerializer

