from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'birth_date', 'profile_picture']
        widgets = {
            'birth_date': forms.DateInput(format='%d.%m.%Y')
        }

class UserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ['username', 'birth_date', 'profile_picture']
        widgets = {
            'birth_date': forms.DateInput(format='%d.%m.%Y')
        }
