from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework.decorators import api_view
from .forms import CustomUserCreationForm, CustomUserSubscribeForm
# from .forms import MobileForm, CodeConfirmForm 
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from django.views import View

from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.shortcuts import render
import twilio
from twilio.rest import Client
import random
# from .utils import send_twilio_message
from .serializers import UserSerializer
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


class SubscribePageView(CreateView):
    form_class = CustomUserSubscribeForm
    success_url = reverse_lazy('subscribe')
    template_name = 'subscribe.html'


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
