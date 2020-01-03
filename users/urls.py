from django.urls import path,include
from .views  import SignUpView, PhoneVerificationView, PhoneVerificationConfirmView
from rest_framework import routers

# router= routers.DefaultRouter() ==> generating tokens
# router.register('tokens', TokenView)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('sendcode/', PhoneVerificationView.as_view(), name='post_new'),
    path('verification/', PhoneVerificationConfirmView.as_view(), name='verification_confirm')
   
]