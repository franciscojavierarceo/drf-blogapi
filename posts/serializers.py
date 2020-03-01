from rest_framework import serializers
from .models import Post
from rest_framework.authtoken.models import Token
# from rest_auth.registration.serializers import RegisterSerializer

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at',)

# class TokenSerializer(serializers.ModelSerializer): ==> Generating tokens

#     class Meta:
#         model = Token
#         fields = ('key', 'user')

# class CustomRegistrationSerializer(RegisterSerializer):

#     def save(self,request):
#         user=super(CustomRegistrationSerializer, self).save(request)
#         user.is_active = False
#         return user

