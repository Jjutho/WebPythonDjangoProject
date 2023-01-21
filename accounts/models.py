from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='images/users', default='')
    age = models.IntegerField(default=18, validators=[MinValueValidator(1), MaxValueValidator(100)])

    def execute_after_login(self):
        pass
