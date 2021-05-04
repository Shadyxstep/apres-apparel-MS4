from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_athletes, name='athletes'),
    path('teams/', views.all_team_members, name='teams'),
    path('<int:athlete_id>', views.athlete_detail, name='athlete_detail'),
]