from django import views
from django.urls import path, include
from clientprofile import views

app_name = 'clientprofile'

urlpatterns = [
    path('client/', views.ClientList_view.as_view()),
    path('client/create/', views.Client_view_post.as_view()),
    path('client/<int:pk>/', views.ClientDetail_view.as_view()),
]
