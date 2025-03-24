from django.contrib.gis.db import models

class PointLocation(models.Model):
    location_name=models.CharField(max_length=100)
    description= models.TextField(blank=True, null=True)
    location_coordinates=models.PointField(geography=True, srid=4326, blank=False, null=False)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural='Locations'
    
    def __str__(self):
        return self.location_name
    
class PopulationDensity(models.Model):
    area_name=models.CharField(max_length=100)
    population=models.IntegerField(blank=False, null=False)
    density=models.FloatField(blank=False, null=False)
    area=models.MultiPolygonField(geography=True, srid=4326, blank=False, null=False)

    class Meta:
        verbose_name_plural='Population_Densities'

    def __str__(self):
        return self.area_name
