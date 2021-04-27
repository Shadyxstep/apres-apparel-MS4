from django.shortcuts import render
from .models import Team, Athletes

# Create your views here.

def all_team_members(request):
    """ A view to show all products, including sorting and search queries """

    Team = Team.objects.all()

    context = {
        'team': Team,
    }

    return render(request, 'team/team.html', context)


def all_athletes(request):
    """ A view to show all products, including sorting and search queries """

    Athletes = Athletes.objects.all()

    context = {
        'athlete': Athletes,
    }

    return render(request, 'athletes/athletes.html', context)