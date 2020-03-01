"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import ThankYouPageView, HomePageView
from allauth.account.views import confirm_email as allauthemailconfirmation
from rest_auth.registration.views import VerifyEmailView,RegisterView
from rest_framework.authtoken import views as rest_framework_views
# from users.views import post_new
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls 
from rest_framework.schemas import get_schema_view

API_TITLE = 'DRF Blog API'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'
schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('thankyou/', ThankYouPageView.as_view(), name='thankyou'),
    path('admin/', admin.site.urls),
    path('posts/api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('swagger-docs/', schema_view)
    # path('new/', include('New_Users.urls')),
    # path('users/', include('users.urls')),
    # path('users/', include('django.contrib.auth.urls')),
    # you CANNOT have this with the others...so i'm commenting it out as a reminder 
        # it will give this error: duplicate key value violates unique constraint "users_customuser_username_key" DETAIL:  Key (username)=() already exists.
    # path('accounts/', include('allauth.urls')),
]
