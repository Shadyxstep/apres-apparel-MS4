from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=254)
    role = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    social_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class Athletes(models.Model):

    class Meta:
        verbose_name_plural = 'Athletes'

    name = models.CharField(max_length=254)
    sport = models.CharField(max_length=254)
    background = models.TextField()
    image = models.ImageField(null=True, blank=True)
    social_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
