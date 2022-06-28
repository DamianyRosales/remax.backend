from django.contrib import admin
from agentprofile.models import UserBase, AgentProfile

# Register your models here.

admin.site.register(UserBase)

admin.site.register(AgentProfile)
