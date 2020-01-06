from django.contrib import admin

# Register your models here.
from .models import New_user, Household
admin.site.register(New_user)
admin.site.register(Household)