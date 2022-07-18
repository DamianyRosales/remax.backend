"""remaxbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from http import client
from django.contrib import admin
from django.urls import path, include

import clientprofile, agentprofile
from agentprofile.jwtviews import EmailTokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('agentprofile.urls', namespace='api-agentprofile')),
    path('api/', include('clientprofile.urls', namespace='api-clientprofile')),
    path('api/', include('officesLocations.urls', namespace='api-officesLocations')),
    path('api/', include('clientOrigin.urls', namespace='api-clientOrigin')),
    
    path('api/auth/login/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh_pair')
]
