from django import views
from django.urls import path, include
from clientOrigin import views

app_name = 'clientOrigin'

urlpatterns = [
    path('clientorigin/', views.ClientOriginListView().as_view()),
]
