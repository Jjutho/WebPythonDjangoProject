from django import forms
from .models import Game, Comment

class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ['title', 'description', 'cover_image', 'product_data_pdf', 'creator', 'release_date', 'genre', 'age_rating', 'price']
        widgets = {
            'genre': forms.Select(choices=Game.GameGenre),
            'age_rating': forms.Select(choices=Game.AgeRatings),
            'user': forms.HiddenInput(),
            'cover_image': forms.FileInput(attrs={
                'accept': '.jpg, .jpeg, .png'}
            ),
            'product_data_pdf': forms.FileInput(attrs={
                'accept': '.pdf'}
            ),
        }

class GameEditForm(forms.ModelForm):

    cover_image = forms.ImageField(required=False)
    product_data_pdf = forms.FileField(required=False)
    class Meta:
        model = Game
        fields = ['title', 'description', 'cover_image', 'product_data_pdf', 'creator', 'release_date', 'genre', 'age_rating', 'price']
        widgets = {
            'genre': forms.Select(choices=Game.GameGenre),
            'age_rating': forms.Select(choices=Game.AgeRatings),
            'user': forms.HiddenInput(),
            'cover_image': forms.FileInput(attrs={
                'accept': '.jpg, .jpeg, .png'}
            ),
            'product_data_pdf': forms.FileInput(attrs={
                'accept': '.pdf'}
            ),
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['rating', 'text']
        widgets = {
            'user': forms.HiddenInput(),
            'game': forms.HiddenInput(),
        }
class SearchForm(forms.ModelForm):

    creator = forms.CharField(required=False)
    title = forms.CharField(required=False)
    genre = forms.ChoiceField(choices=Game.GameGenre.choices, required=False)
    age_rating = forms.ChoiceField(choices=Game.AgeRatings.choices, required=False)

    class Meta:
        model = Game
        fields = ['creator', 'title', 'genre', 'age_rating']
