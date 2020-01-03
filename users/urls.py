from django.urls import path,include
from .views  import SignUpView, PhoneVerificationView, verification_confirm
from rest_framework import routers

# router= routers.DefaultRouter() ==> generating tokens
# router.register('tokens', TokenView)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('sendcode/', PhoneVerificationView.as_view(), name='post_new'),
    path('verification/', verification_confirm, name='verification_confirm')
   
]