from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import HouseholdForm, New_UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import FriendTypeStyle
from django.contrib.auth import get_user_model
import yagmail

User = get_user_model

@login_required
@staff_member_required
def user_form(request):

    if request.method == 'POST':
        form = HouseholdForm(request.POST)
        if form.is_valid():

            data = form.save(commit=False)
            data.FriendType = FriendTypeStyle.get(int(request.POST['FriendType'])).value
            # print(request.user)
            data.User_email_created_by = request.user
            data.Household_name = request.POST['Household_name']
            data.Household_income = request.POST['Household_income']
            print(FriendTypeStyle.get(int(request.POST['FriendType'])).value)
            # print(FriendTypeStyle.int(request.POST['FriendType'].value))
            if str(request.POST['FriendPermission'])== 'on':
                print(True)
                data.FriendPermission = True   
            else:
                print(False)
                data.FriendPermission = False
            
            # print(request.POST['FriendPermission'])
            data.FriendEmail = request.POST['FriendEmail']
            data.save()
            yagmail.register("roughosh47@gmail.com", "babi21091992#")
            yag = yagmail.SMTP(user="roughosh47@gmail.com", password="babi21091992#", host="smtp.gmail.com")
            email = data.FriendEmail
            default_subject = "HouseHold income memeber mail confirmation"
            user = request.user
            contents= ["Hi, {} has added  you as a member to view/edit financial data".format(user)]
            
            # msg = yag.send(email, default_subject,contents)
            yag.send(email, default_subject, contents)
            
            return redirect('thankyou')
    else:
        form = HouseholdForm()
        return render(request, 'household.html', {'form':form})
        # return render(request, 'household_permission.html', {'form':form})


@login_required
def index(request):
    return HttpResponse('Thank you for logging in')