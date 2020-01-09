from django.urls import path
from .views import index, user_form, blog_post

urlpatterns = [
    path('', index, name='index'),
    path('household', user_form, name='user_form'),
    path('household/<int:pk>/', blog_post, name='blog_post')
]
