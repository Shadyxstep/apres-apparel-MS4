from django.shortcuts import render
from .models import Team, Athletes

# Create your views here.

def all_team_members(request):
    """ A view to show all team members """

    teams = Team.objects.all()

    context = {
        'teams': teams,
    }

    return render(request, 'teams/team.html', context)


def all_athletes(request):
    """ A view to show all Apres sponsored athletes"""

    athletes = Athletes.objects.all()

    context = {
        'athletes': athletes,
    }

    return render(request, 'athletes/athletes.html', context)