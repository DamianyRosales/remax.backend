from django.db import models

# Create your models here.

class Office(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.name
