from django.db import models
from agentprofile.models import AgentProfile
from properties.models import Propertie
from officesLocations.models import Office
# Create your models here.

class Trail(models.Model):
    activity_type = 'trail'
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    propertie = models.ForeignKey(Propertie, on_delete=models.CASCADE)
    date = models.DateField()
    trail_date = models.DateField()
    commentaries = models.TextField()
    done = models.BooleanField()

class Call(models.Model):
    activity_type = 'call'
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE)
    propertie = models.ForeignKey(Propertie, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(max_length=255)
    operation = models.CharField(max_length=255)
    commentaries = models.TextField()
    done = models.BooleanField()

class Proposal(models.Model):
    
    activity_type = 'proposal'
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='agent')
    propertie = models.ForeignKey(Propertie, on_delete=models.CASCADE)
    date = models.DateField()
    proposal_date = models.DateField()
    amount = models.IntegerField()
    currency = models.CharField(max_length=255)
    optioning_agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='optioning_agent')
    buyer_office = models.ForeignKey(Office, on_delete=models.CASCADE)
    commentaries = models.TextField()
    done = models.BooleanField()
