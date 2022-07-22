from django import views
from django.urls import path, include
from properties import views

app_name = 'officesLocations'

urlpatterns = [
    path('properties/', views.PropertieListView.as_view()),
    path('properties/filter/', views.PropertieFilterListView.as_view()),
]
