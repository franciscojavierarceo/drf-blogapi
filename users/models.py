from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone

class CustomUser(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    username = models.CharField(max_length=30, unique=True)
    # add additional fields in here

    def __str__(self):
        return self.email
    