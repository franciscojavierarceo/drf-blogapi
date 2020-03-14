from django import forms
from django.contrib.auth import get_user_model
from allauth.account.adapter import get_adapter
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.layout import Submit, Row
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div
from crispy_forms.bootstrap import PrependedText, FormActions, AppendedText, FieldWithButtons

from django.utils.translation import gettext_lazy as _

def get_username(email, splitter="@"):
    try:
        emailparts = email.split(splitter)
        user = emailparts[0]
        domain = ''.join(emailparts[1:]).replace(".", "_")
        username = "{user}_{domain}".format(**{
                "user": user,
                "domain": domain,
            }
        )
        return username
    except:
        return None

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.username = get_username(self.cleaned_data['email'])
        user.save()

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
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = get_username(instance.email)
        instance.set_unusable_password()
        if commit:
            instance.save()
        return instance

    def _get_domain(self, e):
        try:
            d = e.split("@")[1].split(".")[-2].lower()
        except BaseException:
            raise ValidationError("not a valid email")

        return d

    def email_has_valid_domain(self, e):
        domain = self._get_domain(e)
        print('domain = ', domain)
        DOMAINS_NOT_ALLOWED = ['test',]
        return max([domain == d for d in DOMAINS_NOT_ALLOWED]) 

    def clean_username(self):
        print('test username')
        username = self.cleaned_data["username"]
        username = get_adapter().clean_username(username, shallow=False)
        dummy_user = get_user_model()

        if dummy_user and dummy_user.objects.get(username=dummy_user):
            raise forms.ValidationError("not unique")
        # raise forms.ValidationError("User with same email already exist, please change your email")
        return username

    def clean_email(self):
        print('test clean email')
        email = self.cleaned_data["email"]
        email = get_adapter().clean_email(email)
        User = get_user_model()
        if User and User.objects.get(email=email):
            raise forms.ValidationError(_("A user is already registered with this e-mail address."))

        if self.email_has_valid_domain(email):
            raise ValidationError(_("Email is not a part of accepted domains"))

        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        print('test clean', cleaned_data)
        print('test cleaned email', email)
        dummy_user = get_user_model()
        print(dummy_user.objects.all())
        print(dummy_user)
        # dummy_user.objects.filter(username=self.username)
        # print(dummy_user.objects.get(email=dummy_user))
        return cleaned_data
    
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
