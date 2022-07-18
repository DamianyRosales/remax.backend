from django.db import models
from django.core.validators import RegexValidator
from officesLocations.models import Office
from agentprofile.models import AgentProfile
from clientOrigin.models import ClientOrigin

# Create your models here.

class ClientProfile(models.Model):

    email = models.EmailField(max_length=255, unique=True,null=False)
    
    fname = models.CharField(max_length=30, null=False)
    lname = models.CharField(max_length=30, null=False)
    
    homephone = models.CharField(db_column='homephone', max_length=15, blank=True, null=True)

    phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="")
    cellphone = models.CharField(db_column='cellphone',validators=[phone_validator],
                             max_length=17, blank=True,null=False)

    STATUS_CHOICES = (
        (True, 'Activo'),
        (False, 'Inactivo'),
    )
    
    TYPE_CHOICES = (
        (0, 'Tipo 1'),
        (1, 'Tipo 2'),
    )

    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    origin = models.ForeignKey(ClientOrigin, on_delete=models.CASCADE)
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    status = models.BooleanField(choices=STATUS_CHOICES, default=False, null=False)
    typeof = models.IntegerField(choices=TYPE_CHOICES, default=0, null=False)

    notes = models.TextField()

