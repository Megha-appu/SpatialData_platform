from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import PointLocation, PopulationDensity

class MultipointLocationSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = PointLocation
        geo_field = 'location_coordinates'
        fields = ('id', 'location_name', 'description', 'location_coordinates')

    def validate_location_name(self, value):
        if not value:
            raise serializers.ValidationError("location name can't be null.")
        return value
    
    def validate_location_coordinates(self, value):
        if not value:
            raise serializers.ValidationError("location cordinates can't be null.")
        return value


class PopulationDensitySerializer(GeoFeatureModelSerializer):

    class Meta:
        model = PopulationDensity
        geo_field = 'area'
        fields = ('id', 'area_name', 'population', 'density', 'area')
    
    def validate_area_name(self, value):
            if not value:
                raise serializers.ValidationError("Area name can't be null.")
            return value
    
    def validate_population(self, value):
            if not value:
                raise serializers.ValidationError("Population can't be null.")
            return value
    
    def validate_density(self, value):
            if not value:
                raise serializers.ValidationError("Density can't be null.")
            return value
    
    def validate_area(self, value):
            if not value:
                raise serializers.ValidationError("Area cordinates can't be null.")
            return value
    
    
