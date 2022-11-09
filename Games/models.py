from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from datetime import datetime

class Game(models.Model):
    class GameGenre(models.TextChoices):
        FIRSTPERSONSHOOTER = 'FPS', _('First Person Shooter')
        SIMULATION = 'SIM', _('Simulation')
        CITYBUILDER = 'CB', _('City Builder')
        HORRORGAME = 'HG', _('Horror Game')
        ROLEPLAYINGGAME = 'RPG', _('Role Playing Game')
        RACINGGAME = 'RC', _('Racing Game')

    class AgeRatings(models.TextChoices):
        F00 = '0+', _('from 0')
        F06 = '6+', _('from 6')
        F12 = '12+', _('from 12')
        F16 = '16+', _('from 16')
        F18 = '18+', _('from 18')

    # Game title, description, creator and date that the game was released
    title = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.CharField(max_length=100)
    release_date = models.DateTimeField(blank=True, default=datetime.now)

    # Game genre and age rating
    genre = models.CharField(max_length=3, choices=GameGenre.choices)
    age_rating = models.CharField(max_length=3, choices=AgeRatings.choices, default=AgeRatings.F00)

    # User who entered the game into the DB and when
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', related_query_name='user')
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title', 'genre']
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        get_latest_by = "release_date"

    def __str__(self):
        return_string = self.title+', Creator: '+self.creator+', Released: '+self.release_date.strftime("%d.%m.%Y %H:%M:%S")+', Genre: '+self.genre+', Suitable for the ages '+self.age_rating+';'
        return return_string

    def __repr__(self):
        return_string = self.title+'/'+self.creator+'/'+self.release_date.strftime("%d.%m.%Y %H:%M:%S")+'/description('+str(len(self.description))+')/'+self.genre+'/'+self.age_rating
        return return_string
