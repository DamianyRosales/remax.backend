from django.db import models
from django.utils.translation import lazy_number
from officesLocations.models import Office

# Create your models here.

class Image(models.Model):
    propertie_id = models.IntegerField()
    image = models.ImageField(upload_to='REMAXimages/')

class Propertie(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    address = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=255, null=False)
    price = models.IntegerField(null=False)
    size = models.CharField(max_length=255, null=False)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    bedrooms = models.FloatField(null=False)
    bathrooms = models.FloatField(null=False)
    parking_lots = models.IntegerField(null=False)
 
    lt = models.CharField(max_length=255, null=False)
    ln = models.CharField(max_length=255, null=False)

    description = models.TextField()
    typeOfService = models.CharField(max_length=255, null=False)
    areas = models.CharField(max_length=255)

    images = models.ImageField(upload_to='REMAXimages/', null=True, blank=True)

    #images = models.ManyToManyField(Image, null=True)
    def __str__(self):
        return self.address

