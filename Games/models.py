from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.conf import settings

class Game(models.Model):
    class GameGenre(models.TextChoices):
        EMPTY = '', _('Nothing selected')
        FIRSTPERSONSHOOTER = 'FPS', _('First Person Shooter')
        SIMULATION = 'SIM', _('Simulation')
        CITYBUILDER = 'CB', _('City Builder')
        HORRORGAME = 'HG', _('Horror Game')
        ROLEPLAYINGGAME = 'RPG', _('Role Playing Game')
        RACINGGAME = 'RC', _('Racing Game')

    class AgeRatings(models.TextChoices):
        EMPTY = '', _('Nothing selected')
        F00 = '0+', _('from 0')
        F06 = '6+', _('from 6')
        F12 = '12+', _('from 12')
        F16 = '16+', _('from 16')
        F18 = '18+', _('from 18')

    # Game title, description, creator and date that the game was released
    title = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=False)
    creator = models.CharField(blank=False, max_length=100)
    release_date = models.DateTimeField(blank=False, default=datetime.now)
    cover_image = models.ImageField(upload_to='images/games', default='')
    price = models.IntegerField(default=0, blank=False)
    product_data_pdf = models.FileField(upload_to='documents/games', default='')

    # Game genre and age rating
    genre = models.CharField(max_length=4, choices=GameGenre.choices, default=GameGenre.EMPTY)
    age_rating = models.CharField(max_length=4, choices=AgeRatings.choices, default=AgeRatings.EMPTY)

    # User who entered the game into the DB and when
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users', related_query_name='user')
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title', 'genre']
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        get_latest_by = "release_date"

    def __str__(self):
        return_string = self.title+', Creator: '+self.creator+', Released: '+self.release_date.strftime("%d.%m.%Y %H:%M:%S")+', Genre: '+self.genre+', Suitable for the ages '+self.age_rating+'; '+'Price:' + self.price
        return return_string

    def __repr__(self):
        return_string = self.title+'/'+self.creator+'/'+self.release_date.strftime("%d.%m.%Y %H:%M:%S")+'/description('+str(len(self.description))+')/'+self.genre+'/'+self.age_rating+'/'+self.price+'€'
        return return_string

class Comment(models.Model):
    text = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def get_comment_prefix(self):
        if len(self.text) > 50:
            return self.text[:50] + ' ...'
        else:
            return self.text

    def get_upvotes(self):
        upvotes = Vote.objects.filter(up_or_down='U', comment=self)
        return upvotes

    def get_upvotes_count(self):
        return len(self.get_upvotes())

    def get_downvotes(self):
        downvotes = Vote.objects.filter(up_or_down='D', comment=self)
        return downvotes

    def get_downvotes_count(self):
        return len(self.get_downvotes())

    def vote(self, user, up_or_down):
        U_or_D = 'U'
        if up_or_down == 'down':
            U_or_D = 'D'
        vote = Vote.objects.create(up_or_down=U_or_D, user=user, comment=self)

    def __str__(self):
        return self.get_comment_prefix() + ' (' + self.user.username + ')'

    def __repr__(self):
        return self.get_comment_prefix() + ' (' + self.user.username + ' / ' + self.timestamp.strftime("%d.%m.%Y %H:%M:%S") + ')'

class Vote(models.Model):

    VOTE_TYPES = [
        ('U', 'up'),
        ('D', 'down'),
    ]

    def change_vote(self, new_vote):
        self.up_or_down = new_vote

    up_or_down = models.CharField(max_length=1, choices=VOTE_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

