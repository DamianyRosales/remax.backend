from django.db import models
from django.utils.translation import lazy_number
from officesLocations.models import Office

# Create your models here.

class Propertie(models.Model):
    address = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=255, null=False)
    price = models.IntegerField(null=False)
    size = models.CharField(max_length=255, null=False)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    bedrooms = models.IntegerField(null=False)
    bathrooms = models.IntegerField(null=False)
    parking_lots = models.IntegerField(null=False)
    
    lt = models.CharField(max_length=255, null=False)
    ln = models.CharField(max_length=255, null=False)
    
    
    def __str__(self):
        return self.address
