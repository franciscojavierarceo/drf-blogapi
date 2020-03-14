from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.layout import Submit, Row
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div
from crispy_forms.bootstrap import PrependedText, FormActions, AppendedText, FieldWithButtons

from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserSubscribeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', )
    
    email = forms.EmailField(
        label=_(''),
        widget=forms.TextInput(
                attrs={
                    'placeholder': _('john@email.com')
                    }
            )
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper =  FormHelper()
        self.helper.form_show_labels = False
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-inline justify-content-center'
        self.helper.layout = Layout(
            Div(
                FieldWithButtons('email', Submit('Submit', 'submit', css_class='btn btn-outline primary')),
                Submit('submit', u'Submit', css_class='btn btn-success'),
                 css_class='form-inline'
            )
        )

# class CustomUserSubscribeForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = (
#             # 'username', 
#             'email',
#         )

#     # email = forms.EmailField(
#     #     label='email',
#     #     widget=forms.TextInput(
#     #             attrs={
#     #                 'placeholder': 'john@email.com'
#     #                 }
#     #         )
#     # )
#     # password = forms.CharField(
#     #     label='password',
#     #     widget=forms.PasswordInput(
#     #         attrs={
#     #             'placeholder': 'password'
#     #         }
#     #     )
#     # )
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper =  FormHelper(self)
#         self.helper.form_show_labels = False
#         self.helper.form_method = 'POST'

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         instance.set_unusable_password()
#         if commit:
#             instance.save()
#         return instance
