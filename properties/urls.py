from django import views
from django.urls import path, include, re_path
from properties import views

app_name = 'officesLocations'

urlpatterns = [
    path('properties/', views.PropertieListView.as_view()),
    path('properties/filter/', views.PropertieFilterListView.as_view()),
    #url(r'properties/filter/(?P<address>\w+)/(?P<typeP>\w+)/(?P<priceGTE>\w+)/(?P<priceLTE>\w+)/(?P<sizeGTE>\w+)/(?P<sizeLTE>\w+)/(?P<bedrooms>\w+)/(?P<bathrooms>\w+)/(?P<parking_lots>\w+)/$', views.PropertieFilterListView.as_view()),
    #re_path(r'^properties/filter/(?P<address>\d+)$', views.PropertieFilterListView.as_view()),

    #re_path(r'properties/filter/<address>/', views.PropertieFilterListView.as_view()),
]
