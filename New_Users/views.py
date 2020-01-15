from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import HouseholdForm, New_UserForm, HouseholdRedirectForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import FriendTypeStyle
from django.contrib.auth import get_user_model
from .serializers import HouseholdSerializers
from .models import Household
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views import View
# from braces.views import CsrfExemptMixin
User = get_user_model()


class FormVerificationView(View):

    template_name = "household.html"
    form_class = HouseholdForm 
    context = {}

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context.update({'form':form})
        return render(request, self.template_name , self.context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        
        if form.is_valid():

            data = form.save(commit=False)
            data.FriendType = FriendTypeStyle.get(int(request.POST['FriendType'])).value
            name=request.POST['name']
            data.User_email_created_by = request.user
            print(FriendTypeStyle.get(int(request.POST['FriendType'])).value)
            
            if str(request.POST.get('FriendPermission')) == 'on':
                print(True)
                data.FriendPermission = True   
            else:
                print(False)
                data.FriendPermission = False

            data.FriendEmail = request.POST['FriendEmail']
            # pk = self.kwargs['pk']
            pk = data.pk
            print(pk)
            flag=0
            print(list(User.objects.all()))
            user_list = list(User.objects.all().values('email'))
            print(list(User.objects.all().values('email')))

            for values in range(len(user_list)):
                if user_list[values]['email'] == request.POST['FriendEmail']:
                    print('Success you email is {}'.format(user_list[values]['email']))
                    flag=1
                    break
            if flag==1:
                print('check')
                user =request.user
                Subject = 'Hi, this an automated mail sent'
                Body = "Hi {}, {} has invited you to log in as a member to view/edit financial data, Go to the page: <a href='http://0.0.0.0:8000/new/household/'>click here</a>".format(name,user)
                required = 0
                send_mail(
                            Subject,
                            Body,
                            settings.EMAIL_HOST_USER,
                            [data.FriendEmail],
                            fail_silently=False,
                        )
                print('message succeeded')
            
            else:

                print('did not enter')
                print ('data_not_present in database')
                required =1
                user =request.user
                Subject = 'Hi, this an automated mail sent'
                Body= "Hi {}, {} has invited you to log in as a member to view/edit financial data, Go to the page: <a href='http://0.0.0.0:8000/accounts/signup/'>click here</a>".format(name,user)
                send_mail(
                            Subject,
                            Body,
                            settings.EMAIL_HOST_USER,
                            [data.FriendEmail],
                            fail_silently=False,
                        )
                print('message failed')
                # return redirect('user_form')
            
            return redirect('thankyou')
        else:
            form = HouseholdForm()
            return render(request, 'household.html', {'form':form})        

@login_required
def index(request):

    return HttpResponse('Thank you for logging in')

class BlogPostVerificationView(View):

    template_name = 'household_redirect.html'
    form_class = HouseholdRedirectForm 
    context = {}

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        
        obj = get_object_or_404(Household, pk=kwargs['pk'])
        form = self.form_class(instance=obj)
        self.context.update({'form':form})
        return render(request, self.template, self.context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        obj = get_object_or_404(Household, pk=kwargs['pk'])
        form = self.form_class(request.POST, instance=obj)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.Household_income = request.POST['Household_income']

            obj.save()
            return redirect("/")
        return redirect("/")
        # else:
        #     form = HouseholdRedirectForm(instance=obj)
        #     return render(request, self.template_name, {'form':form})
        # self.context.update({'form':form})
        # return render(request, self.template, self.context)

# @login_required
# def blog_post(request, pk):
    
#     obj = get_object_or_404(Household, pk=pk)
    
#     if request.method == 'POST':
#         form = HouseholdRedirectForm(request.POST, instance=obj)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.Household_income = request.POST['Household_income']

#             obj.save()
#             return redirect("/")
#     else:
#         form = HouseholdRedirectForm(instance=obj)
#         return render(request, 'household_redirect.html', {'form':form})

def send_email(request, val1,val2):
    
    print('you have entered send_mail')
    
    value=val1
    Email = val2
    print('This is inside send_mail')
    print(val1)
    print(val2)
    
    Subject = 'Hi, this an automated mail sent'
    Body = "Hi, admin invited you to log in as a member to view/edit financial data, Go to the page: <a href='http://0.0.0.0:8000/new/snippets/{}'>click here</a>".format(value)
    send_mail(
                Subject,
                Body,
                settings.EMAIL_HOST_USER,
                [Email],
                fail_silently=False,
            )
    print('message succeeded')

def send_email_link(request, val2):
    
    print('you have entered send_mail_link')

    Email = val2
    print('This is inside send_mail_link')
    print(val2)

    Subject = 'Hi, this an automated mail sent'
    Body = "Hi, admin invited you to log in as a member to view/edit financial data, Kindly sign up and Go to the page: <a href='http://0.0.0.0:8000/api/v1/rest-auth/registration/'>click here</a>"
    
    send_mail(
                Subject,
                Body,
                settings.EMAIL_HOST_USER,
                [Email],
                fail_silently=False,
            )
    print('message succeeded')

class HouseholdList(generics.ListCreateAPIView):
    
    queryset = Household.objects.all()
    serializer_class = HouseholdSerializers


    def get(self, request, *args, **kwargs):

        print("Success")
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        Value1=[]
        Var= self.create(request, *args, **kwargs)
        print(Var.data)
        val1=Var.data['id']
        val2=Var.data['FriendEmail']
        print(Var.data['id'])
        print(val2)
        
        print('breaking point')
        print(list(User.objects.all().values('email')))
        User_list = list(User.objects.all().values('email'))
        for values in range(len(User_list)):
            if User_list[values]['email'] == val2:
                print("exists")
                send_email(request, val1, val2)
                break
            else:
                print("does not exists")
                send_email_link(request, val2)    
        return Var

class HouseholdDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Household.objects.all()
    serializer_class = HouseholdSerializers

@api_view()
def hello(request):
    return Response({"message": "Hello, world"})