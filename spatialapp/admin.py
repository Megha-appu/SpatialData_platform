from django.contrib.gis import admin
from .models import PointLocation,PopulationDensity

@admin.register(PointLocation)
class MultipointLocationAdmin(admin.GISModelAdmin):  # GeoModelAdmin for handling geospatial fields
    list_display = ('location_name', 'description', 'location_coordinates')  # Fixed typo in 'discription' and 'location_cordinates'
    search_fields = ('location_name',)  # Allows search by location name

# Register the PopulationDensity model with the admin
@admin.register(PopulationDensity)
class PopulationDensityAdmin(admin.GISModelAdmin):  # GeoModelAdmin for handling geospatial fields
    list_display = ('area_name', 'population', 'density', 'area')  # Shows area name, population, density, and area
    search_fields = ('area_name', 'population')  # Allows search by area name and population
    list_filter = ['population', 'density']  # Filters by population and density
