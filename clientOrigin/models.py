from django.db import models

# Create your models here.

class ClientOrigin(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
