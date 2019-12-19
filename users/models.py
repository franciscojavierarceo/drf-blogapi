from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    # pass
    username=models.CharField(max_length=30, unique=False)
    # add additional fields in here

    def __str__(self):
        return self.username
    
    