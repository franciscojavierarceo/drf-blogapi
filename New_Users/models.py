from django.db import models
from django.conf import settings
from django_enumfield import enum
# Create your models here.

class EmploymentStyle(enum.Enum):

    FullTime = 0
    PartTime = 1
    Unemployed = 2
    SelfEmployed = 3

class EducationStyle(enum.Enum):

    College = 0
    School = 1
    GraduateSchool = 2
    TradeSchool = 3

class FriendTypeStyle(enum.Enum):

    Partner = 0
    Child = 1
    Sibling = 2
    Parent = 3
    Other = 4

class New_user(models.Model):

    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Job_title = models.CharField(max_length=30)
    Employer = models.CharField(max_length=30)
    Income = models.IntegerField()

    Employment_type = enum.EnumField(EmploymentStyle, default=EmploymentStyle.PartTime)
    Education = enum.EnumField(EducationStyle, default = EducationStyle.College)
    ZipCode = models.IntegerField()

    def __str__(self):
        return self.Job_title

class Household(models.Model):

    User_email_created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    Household_name = models.CharField(max_length=100)
    Household_income = models.IntegerField()
    # CHOICES={}
    # FriendType = models.CharField(max_length=2, Choices=((0, ('FullTime')), (1, ('PartTime')), (2,('Unemployed')), (3, ('SelfEmployed'))))
    
    FriendType = enum.EnumField(FriendTypeStyle, default = FriendTypeStyle.Partner)
    FriendPermission = models.BooleanField(default=False)
    FriendEmail = models.EmailField()

    def __str__(self):
        return self.Household_name
