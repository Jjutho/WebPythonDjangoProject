from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    profile_picture = models.ImageField(upload_to='images/users', default='')
    age = models.IntegerField(default=18, validators=[MinValueValidator(1), MaxValueValidator(100)])
    email = models.EmailField(default='')

    def execute_after_login(self):
        pass
