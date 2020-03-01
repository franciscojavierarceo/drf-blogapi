from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.


User = get_user_model()

class PhoneVerification(models.Model):
    
    Username = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30, default= None, null=True, blank=True)
    verification_code = models.IntegerField(default=None, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.phone_number