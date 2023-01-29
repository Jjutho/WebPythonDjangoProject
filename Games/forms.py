from django import forms
from .models import Game, Comment

class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ['title', 'description', 'cover_image', 'creator', 'release_date', 'genre', 'age_rating']
        widgets = {
            'genre': forms.Select(choices=Game.GameGenre),
            'age_rating': forms.Select(choices=Game.AgeRatings),
            'user': forms.HiddenInput(),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'user': forms.HiddenInput(),
            'game': forms.HiddenInput(),
        }
class SearchForm(forms.ModelForm):

    title = forms.CharField(required=False)

    class Meta:
        model = Game
        fields = ['creator', 'title']