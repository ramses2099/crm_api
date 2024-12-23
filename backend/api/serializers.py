from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'is_staff']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model= Status
        fields = '__all__'


class CustomerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomerType
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerEmail
        fields = '__all__'

class CustomerPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPhone
        fields = '__all__'

class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = '__all__'
