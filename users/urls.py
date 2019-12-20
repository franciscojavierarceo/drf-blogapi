from django.urls import path,include
from .views  import SignUpView
from rest_framework import routers

# router= routers.DefaultRouter() ==> generating tokens
# router.register('tokens', TokenView)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    

]