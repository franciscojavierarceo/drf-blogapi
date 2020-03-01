from django import forms
from .models import PhoneVerification

class PhoneVerificationForm(forms.ModelForm):

    class Meta:
        model = PhoneVerification
        fields = ('phone_number',)

class CodeConfirmForm(forms.ModelForm):

    class Meta:
        model = PhoneVerification
        fields = ('verification_code',)