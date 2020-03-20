from django.urls import path,include
from .views import SignUpView, SubscribePageView
# CustomSignUpView
from rest_framework import routers
from .views import UserDetail, UserList

# router= routers.DefaultRouter() ==> generating tokens
# router.register('tokens', TokenView)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='account_signup_custom'),  
    # Do not use this
    # path('custom_signup/', CustomSignUpView.as_view(), name='account_signup_custom'),  
    path('subscribe', SubscribePageView.as_view(), name='account_subscribe'),  
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]