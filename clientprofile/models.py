from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class ClientProfile(models.Model):

    email = models.EmailField(max_length=255, unique=True,null=False)
    
    fname = models.CharField(max_length=30, null=False)
    lname = models.CharField(max_length=30, null=False)
    
    homephone = models.CharField(db_column='homephone', max_length=15, blank=True, null=True)

    phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="")
    cellphone = models.CharField(db_column='cellphone',validators=[phone_validator],
                             max_length=17, blank=True,null=False)

    OFFICE_CHOICES = (
        (0, "RE/MAX México"),
    )

    ORIGIN_CHOICES = (
        (0, 'SIR || Tarjeta Digital'),
    )

    AGENT_CHOICES = (
        (0, 'Dinorah Felgueres Hernández'),
        (1, 'Eduardo Cruz García'),
        (2, 'Felipe Gonzalez Rosales'),
        (3, 'Salvador Haro Cisneros'),
    )

    STATUS_CHOICES = (
        (True, 'Activo'),
        (False, 'Inactivo'),
    )
    
    TYPE_CHOICES = (
        (0, 'Tipo 1'),
        (1, 'Tipo 2'),
    )

    office = models.IntegerField(choices=OFFICE_CHOICES, default=0, null=False)
    origin = models.IntegerField(choices=ORIGIN_CHOICES, default=0, null=False)
    agent = models.IntegerField(choices=AGENT_CHOICES, default=0, null=False)
    status = models.BooleanField(choices=STATUS_CHOICES, default=False, null=False)
    typeof = models.IntegerField(choices=TYPE_CHOICES, default=0, null=False)

    notes = models.TextField()

