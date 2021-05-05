from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Team, Athletes
from .forms import AthleteForm, TeamForm


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
    """A view to show an individual athlete"""
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


@login_required
def edit_athlete(request, athlete_id):
    """ Edit a athlete profile in the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you do not have\
                 authorisation for that action.'
                 )
        return redirect(reverse('home'))

    athlete = get_object_or_404(Athletes, pk=athlete_id)
    if request.method == 'POST':
        form = AthleteForm(request.POST, request.FILES, instance=athlete)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Athlete!')
            return redirect(reverse('athlete_detail', args=[athlete.id]))
        else:
            messages.error(
                request, 'Failed to update product.\
                     Please ensure the form is valid.'
                     )
    else:
        form = AthleteForm(instance=athlete)
        messages.info(request, f'You are editing {athlete.name}')

    template = 'athletes/edit_athlete.html'
    context = {
        'form': form,
        'athlete': athlete,
    }

    return render(request, template, context)


@login_required
def delete_athlete(request, athlete_id):
    """ Delete an athlete """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    athlete = get_object_or_404(Athletes, pk=athlete_id)
    athlete.delete()
    messages.success(request, f'{athlete.name} deleted!')
    return redirect(reverse('athletes'))


def team_detail(request, team_id):
    """A view to show individual team member"""
    team = get_object_or_404(Team, pk=team_id)

    context = {
        'team': team,
    }

    return render(request, 'teams/team_detail.html', context)


@login_required
def add_team(request):
    """ Add another team member to the site"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            team = form.save()
            messages.success(request, f'Successfully added {team.name}!')
            return redirect(reverse('team_detail', args=[team.id]))
        else:
            messages.error(request,
                           'Failed to add team member.'
                           'Please ensure the form is valid.')
    else:
        form = TeamForm()

    template = 'teams/add_team.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_team(request, team_id):
    """ Edit a team member in the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you do not have\
                 authorisation for that action.'
                 )
        return redirect(reverse('home'))

    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Team Member!')
            return redirect(reverse('team_detail', args=[team.id]))
        else:
            messages.error(
                request, 'Failed to update team member details.\
                     Please ensure the form is valid.'
                     )
    else:
        form = TeamForm(instance=team)
        messages.info(request, f'You are editing {team.name}')

    template = 'teams/edit_team.html'
    context = {
        'form': form,
        'team': team,
    }

    return render(request, template, context)


@login_required
def delete_team(request, team_id):
    """ Delete a team member """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    team = get_object_or_404(Team, pk=team_id)
    team.delete()
    messages.success(request, f'{team.name} deleted!')
    return redirect(reverse('teams'))
