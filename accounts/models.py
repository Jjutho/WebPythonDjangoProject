from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='images/users', default='')
    birth_date = models.DateField(null=True, blank=True)
