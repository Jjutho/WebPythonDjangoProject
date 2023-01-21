from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

from .forms import SignUpForm, UserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['username', 'password', 'birth_date', 'profile_picture']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('birth_date', 'profile_picture')}),
    )

admin.site.register(CustomUser, UserAdmin)