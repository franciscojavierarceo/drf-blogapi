from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class MobileForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('phone_number',)

class CodeConfirmForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('verification_code',)

