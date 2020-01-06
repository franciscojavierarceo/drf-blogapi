from django.urls import path
from .views import index, user_form

urlpatterns = [
    path('', index, name='index'),
    path('household', user_form, name='user_form')
]
