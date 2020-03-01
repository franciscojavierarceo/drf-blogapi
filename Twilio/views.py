from django.shortcuts import render
from .forms import PhoneVerificationForm, CodeConfirmForm
from django.contrib.auth import get_user_model
import random
import twilio
from .utils import send_twilio_message
from django.views import View
# Create your views here.

User = get_user_model()

class PhoneVerificationView(View):
    template_name = 'verification.html'
    form_class =  PhoneVerificationForm
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
            form = PhoneVerificationForm()
        return render(request, 'verification.html', {'form': form})

class PhoneVerificationConfirmView(View):
    template_name = 'confirmation.html'
    form_class =  CodeConfirmForm
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context.update({'form': form})
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.verification_code = request.POST['verification_code']
            print(post.verification_code)
            verified_number = User.objects.all().values('verification_code').last()
            print(verified_number['verification_code'])
            if str(verified_number['verification_code']) == post.verification_code:
                return redirect('thankyou')
            else:
                # we should probably trigger an error here or not redirect
                print('code entered did not match sent!')
                return redirect('/')
        else:
            form = CodeConfirmForm()
            return render(request, 'confirmation.html', {'form': form})