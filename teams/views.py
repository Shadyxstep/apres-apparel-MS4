from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Team, Athletes


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


def athlete_detail(request, athlete_id):
    """A view to show individual blog post"""
    athlete = get_object_or_404(Athletes, pk=athlete_id)

    context = {
        'athlete': athlete,
    }

    return render(request, 'athletes/athlete_detail.html', context)
