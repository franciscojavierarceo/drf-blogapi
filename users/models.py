from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone

class CustomUser(AbstractUser):
    # pass
    username=models.CharField(max_length=30, unique=True)
    # add additional fields in here
    phone_number = models.CharField(max_length=30, default= None, null=True, blank=True)
    verification_code = models.IntegerField(default=None, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
    
    