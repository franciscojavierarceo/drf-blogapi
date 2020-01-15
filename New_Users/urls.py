from django.urls import path
from .views import index, FormVerificationView, BlogPostVerificationView, HouseholdList, HouseholdDetail, hello
# from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('', index, name='index'),
    path('household', FormVerificationView.as_view(), name='Form_verification'),
    path('household/<int:pk>/', BlogPostVerificationView.as_view(), name='blog_post'),
    path('snippets/', HouseholdList.as_view(), name='householdlist'),
    path('snippets/<int:pk>/', HouseholdDetail.as_view(), name='householddetail'),
    path('hello/', hello),
]
