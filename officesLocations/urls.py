from django import views
from django.urls import path, include
from officesLocations import views

app_name = 'officesLocations'

urlpatterns = [
    path('offices/', views.OfficeListView.as_view()),
]
