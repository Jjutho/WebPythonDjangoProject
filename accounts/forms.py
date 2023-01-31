from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age', 'profile_picture']
        widgets = {
            'profile_picture': forms.FileInput(attrs={
                'accept': '.jpg, .jpeg, .png'}
            ),
        }

class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ['username', 'email', 'age', 'profile_picture']
        widgets = {
            'profile_picture': forms.FileInput(attrs={
                'accept': '.jpg, .jpeg, .png'}
            ),
        }
