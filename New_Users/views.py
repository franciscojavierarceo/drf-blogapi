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
from email.mime.text import MIMEText

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
            data.Household_name = request.POST['Household_name']
            data.Household_income = request.POST['Household_income']
            print(FriendTypeStyle.get(int(request.POST['FriendType'])).value)
            
            if str(request.POST.get('FriendPermission')) == 'on':
                print(True)
                data.FriendPermission = True   
            else:
                print(False)
                data.FriendPermission = False

            data.FriendEmail = request.POST['FriendEmail']
            data.save()
            yagmail.register("roughosh47@gmail.com", "babi21091992#")
            yag = yagmail.SMTP(user="roughosh47@gmail.com", password="babi21091992#", host="smtp.gmail.com")
            email = data.FriendEmail
            default_subject = "HouseHold income member mail confirmation"
            user = request.user
            contents= ["Hi {}, {} has added  you as a member to view/edit financial data, Go to the page: <a href='http://0.0.0.0:8000/new/household/{}/'>click here</a>".format(name,user,data.pk)]
            yag.send(email, default_subject, contents)
            
            #email verification
            print(list(User.objects.all()))
            user_list = list(User.objects.all().values('email'))
            print(list(User.objects.all().values('email')))

            for values in range(len(user_list)):
                if user_list[values]['email'] == request.POST['FriendEmail']:
                    print('Success you email is {}'.format(user_list[values]['email']))
                    return redirect('home')
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