from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_athletes, name='athletes'),
    path('teams/', views.all_team_members, name='teams'),
    path('<int:athlete_id>', views.athlete_detail, name='athlete_detail'),
    path('add/', views.add_athlete, name='add_athlete'),
    path('edit/<int:athlete_id>', views.edit_athlete, name='edit_athlete'),
    path('delete/<int:athlete_id>', views.delete_athlete,
         name='delete_athlete'),
]
