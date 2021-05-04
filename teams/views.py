from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Team, Athletes
from .forms import AthleteForm


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


@login_required
def add_athlete(request):
    """ Add another athlete to the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AthleteForm(request.POST, request.FILES)
        if form.is_valid():
            athlete = form.save()
            messages.success(request, f'Successfully added {athlete.name}!')
            return redirect(reverse('athlete_detail', args=[athlete.id]))
        else:
            messages.error(request,
                           'Failed to add athlete.'
                           'Please ensure the form is valid.')
    else:
        form = AthleteForm()

    template = 'athletes/add_athlete.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
