from rest_framework import serializers
from .models import Household

class HouseholdSerializers(serializers.ModelSerializer):

    class Meta:
        model = Household
        fields = ('User_email_created_by','FriendType', 'Household_income', 'Household_name',
                'FriendPermission', 'FriendEmail',)

        
