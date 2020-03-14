from django.urls import path,include
from .views  import SignUpView, SubscribePageView
from rest_framework import routers
from .views import UserDetail, UserList

# router= routers.DefaultRouter() ==> generating tokens
# router.register('tokens', TokenView)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),  
    path('subscribe', SubscribePageView.as_view(), name='subscribe'),  
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]