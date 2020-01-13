from django.urls import path
from .views import PhoneVerificationConfirmView, PhoneVerificationView

urlpatterns = [
        path('sendcode/', PhoneVerificationView.as_view(), name='post_new'),
        path('verification/', PhoneVerificationConfirmView.as_view(), name='verification_confirm')
]