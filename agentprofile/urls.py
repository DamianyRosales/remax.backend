from django.urls import path
from agentprofile import views

app_name = 'agentprofile'

urlpatterns = [
    path('agent/', views.agent_view.as_view()),
    path('agent/create/', views.agent_view_post.as_view()),
    path('agent/states/', views.States.as_view()),
    path('agent/offices/', views.Offices.as_view()),
]
