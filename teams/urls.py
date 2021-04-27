from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_athletes, name='athletes'),
    path('', views.all_team_members, name='teams'),
]