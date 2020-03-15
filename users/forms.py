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

class PasswordField(forms.CharField):

    def __init__(self, *args, **kwargs):
        render_value = kwargs.pop('render_value', False)
        kwargs['widget'] = forms.PasswordInput(render_value=render_value,
                                               attrs={'placeholder':
                                                      kwargs.get("label")})
        super(PasswordField, self).__init__(*args, **kwargs)

class SetPasswordField(PasswordField):

    def __init__(self, *args, **kwargs):
        super(SetPasswordField, self).__init__(*args, **kwargs)
        self.user = None

    def clean(self, value):
        value = super(SetPasswordField, self).clean(value)
        value = get_adapter().clean_password(value, user=self.user)
        return value

# This is the correct version
# Note it does NOT require a view
class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email')
    
    # Use this for creation here
    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.username = get_username(self.cleaned_data['email'])
        user.save()


class MyCustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password1',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # For forms.ModelForm, you have to use .save()
    # note this accurately sets the password using allauth
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.username = get_username(instance.email)
        instance.set_password(self.cleaned_data['password1'])
        if commit:
            instance.save()
        return instance

    email = forms.EmailField(
        label=_('E-mail'),
        widget=forms.TextInput(
                attrs={
                    'placeholder': _('E-mail address')
                    }
            )
    )

    password1 = PasswordField(label=_("Password"))

    def _get_domain(self, e):
        try:
            d = e.split("@")[1].split(".")[-2].lower()
        except BaseException:
            raise ValidationError("not a valid email")

        return d

    def email_has_valid_domain(self, e):
        domain = self._get_domain(e)
        DOMAINS_NOT_ALLOWED = ['test',]
        return max([domain == d for d in DOMAINS_NOT_ALLOWED]) 

    def clean_username(self):
        username = self.cleaned_data["username"]
        username = get_adapter().clean_username(username, shallow=False)
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        email = get_adapter().clean_email(email)
        User = get_user_model()
        if User:
            try:
                if User.objects.get(email=email):
                    raise forms.ValidationError(_("A user is already registered with this e-mail address."))
            except Exception as e:
                pass

        if self.email_has_valid_domain(email):
            raise ValidationError(_("Email is not a part of accepted domains"))

        return email

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data["password1"]
        User = get_user_model()
        if password:
            try:
                get_adapter().clean_password(password, user=User)
            except forms.ValidationError as e:
                self.add_error('password1', e)
        return cleaned_data

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
        DOMAINS_NOT_ALLOWED = ['test',]
        return max([domain == d for d in DOMAINS_NOT_ALLOWED]) 

    def clean_username(self):
        username = self.cleaned_data["username"]
        username = get_adapter().clean_username(username, shallow=False)
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        email = get_adapter().clean_email(email)
        User = get_user_model()
        if User:
            try:
                if User.objects.get(email=email):
                    raise forms.ValidationError(_("A user is already registered with this e-mail address."))
            except Exception as e:
                pass

        if self.email_has_valid_domain(email):
            raise ValidationError(_("Email is not a part of accepted domains"))

        return email

    def clean(self):
        cleaned_data = super().clean()
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
