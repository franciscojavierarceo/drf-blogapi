from django.urls import path
from .views import index, user_form, blog_post, HouseholdList, HouseholdDetail, hello

urlpatterns = [
    path('', index, name='index'),
    path('household', user_form, name='user_form'),
    path('household/<int:pk>/', blog_post, name='blog_post'),
    path('snippets/', HouseholdList.as_view(), name='householdlist'),
    path('snippets/<int:pk>/', HouseholdDetail.as_view(), name='householddetail'),
    path('hello/', hello),
]
