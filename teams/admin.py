from django.contrib import admin
from .models import Team, Athletes


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'role',
        'image',
        'social_url',
    )


class AthleteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sport',
        'background',
        'image',
        'social_url',
    )

admin.site.register(Team, TeamAdmin)
admin.site.register(Athletes, AthleteAdmin)