from rest_framework import serializers
from .models import Household

class HouseholdSerializers(serializers.ModelSerializer):

    class Meta:
        model = Household
        fields = ('FriendType', 'Household_income', 'Household_name',
                'FriendPermission', 'FriendEmail',)
