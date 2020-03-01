from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import HouseholdForm, New_UserForm, HouseholdRedirectForm
from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required
from .models import FriendTypeStyle
from django.contrib.auth import get_user_model
import yagmail
from .serializers import HouseholdSerializers
from .models import Household
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

User = get_user_model()

@login_required
def user_form(request):

    if request.method == 'POST':
        form = HouseholdForm(request.POST)
        if form.is_valid():

            data = form.save(commit=False)
            data.FriendType = FriendTypeStyle.get(int(request.POST['FriendType'])).value
            name=request.POST['name']
            data.User_email_created_by = request.user
            # data.Household_name = request.POST['Household_name']
            # data.Household_income = request.POST['Household_income']
            print(FriendTypeStyle.get(int(request.POST['FriendType'])).value)
            
            if str(request.POST.get('FriendPermission')) == 'on':
                print(True)
                data.FriendPermission = True   
            else:
                print(False)
                data.FriendPermission = False

            data.FriendEmail = request.POST['FriendEmail']
            # data.save()
            
            
            flag=0
            #email verification
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
                Body = "Hi {}, {} has invited you to log in as a member to view/edit financial data, Go to the page: <a href='http://0.0.0.0:8000/new/household/{}'>click here</a>".format(name,user,data.pk)
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

@login_required
def blog_post(request, pk):
    
    obj = get_object_or_404(Household, pk=pk)
    
    if request.method == 'POST':
        form = HouseholdRedirectForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.Household_income = request.POST['Household_income']

            obj.save()
            return redirect("/")

    else:
        form = HouseholdRedirectForm(instance=obj)
        return render(request, 'household_redirect.html', {'form':form})

def send_email():
        
        # user =HouseholdSerializers.User_email_created_by
        Subject = 'Hi, this an automated mail sent'
        Body = "Hi, admin invited you to log in as a member to view/edit financial data, Go to the page: <a href='http://0.0.0.0:8000/new/snippets/'>click here</a>"
        required = 0
        send_mail(
                    Subject,
                    Body,
                    settings.EMAIL_HOST_USER,
                    [HouseholdSerializers.FriendEmail],
                    fail_silently=False,
                )
        print('message succeeded')

class HouseholdList(generics.ListCreateAPIView):
    
    queryset = Household.objects.all()
    serializer_class = HouseholdSerializers(queryset, many=True)

    def get_field_names(self, *args, **kwargs):
        
        field_names = self.context.get('FriendEmail', None)
        if field_names:
            return field_names
        return super(self).get_field_names(*args, **kwargs)

    def create(self, request, *args, **kwargs):

        response = super(HouseholdList, self).create(request, *args, **kwargs)
        send_email()  # sending mail
        return response
    

class HouseholdDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Household.objects.all()
    serializer_class = HouseholdSerializers

    

@api_view()
def hello(request):
    return Response({"message": "Hello, world"})