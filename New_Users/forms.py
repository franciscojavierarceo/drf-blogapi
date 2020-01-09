from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import New_user, Household

class New_UserForm(forms.ModelForm):

    class Meta:
        model = New_user
        fields = ('Job_title',)

class HouseholdForm(forms.ModelForm):

    FriendPermission = forms.BooleanField(required=False)
    class Meta:
        model = Household
        fields = ('FriendType', 'Household_income', 'Household_name','FriendPermission', 'FriendEmail')

class HouseholdRedirectForm(forms.ModelForm):

    class Meta:
        model = Household
        fields = ('Household_income',)