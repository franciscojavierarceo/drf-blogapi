from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework.decorators import api_view
from .forms import CustomUserCreationForm
from .forms import MobileForm, CodeConfirmForm 
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from django.views import View

from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.shortcuts import render
import twilio
from twilio.rest import Client
import random
from .utils import send_twilio_message
from django.contrib.auth import get_user_model

User=get_user_model()

# account_sid= key_twilio.account_sid
# account_token=key_twilio.account_token

# tel=key_twilio.tel
# twil=key_twilio.twil


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class PhoneVerificationView(View):
    template_name = 'verification.html'
    form_class = MobileForm 
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context.update({'form': form})
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.phone_number = request.POST['phone_number']
            r1 = random.randint(99999, 1000000)
            post.verification_code=r1
            sms = send_twilio_message(post.phone_number, r1)
            post.save()
            #print('code sent to database')
            return redirect('verification_confirm')
        else:
            form = CodeConfirmForm()
        return render(request, 'verification.html', {'form': form})


def verification_confirm(request):

    if request.method == 'POST':

        form = CodeConfirmForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.verification_code = request.POST['verification_code']
            print(post.verification_code)
            verified_number = User.objects.all().values('verification_code').last()
            print(verified_number['verification_code'])
            if str(verified_number['verification_code']) == post.verification_code:
                return redirect('thankyou')
            else:
                return redirect('/')
    else:

        form = CodeConfirmForm()
        return render(request, 'confirmation.html', {'form':form})

