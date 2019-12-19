from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework.decorators import api_view
from .forms import CustomUserCreationForm
from rest_framework import status
from rest_framework.response import Response
# from .serializers import TokenSerializer
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.shortcuts import render

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# class TokenView(viewsets.ModelViewSet): ==>Generating tokens
#     queryset= Token.objects.all()
#     serializer_class =TokenSerializer

# def index(request):  ===>> Demo test
#     send_mail('Hello from capitalnumbers','Hello, this is an automated message',
#     'rounak@capitalnumbers.com', ['piwohom684@mail3x.net'], fail_silently=False)
#     return render(request,'index.html')

