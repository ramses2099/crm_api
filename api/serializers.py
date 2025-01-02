from django.contrib.auth.models import User
from rest_framework import serializers

from .models import (
    Customer,
    CustomerAddress,
    CustomerEmail,
    CustomerPhone,
    CustomerType,
    Status,
)

# Serializers define the API representation.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'id','username', 'email', 'is_staff']


class StatusSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
  
    class Meta:
        model= Status
        fields = ['status_id', 
                    'description',
                    'user', 
                    'updated',
                    'created']


class CustomerTypeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model= CustomerType
        fields = ['customertype_id','description',
                    'user',
                    'status',
                    'updated',
                    'created',]

class CustomerSerializer(serializers.ModelSerializer):
    customertype = CustomerTypeSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = [            
            'customer_id','firstname','lastname','customertype','user','status','updated','created'
        ]

class CustomerEmailSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customertype = CustomerTypeSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    class Meta:
        model = CustomerEmail
        fields = [
            'customeremail_id','email','customer','customertype','user','status','updated','created'
              ]

class CustomerPhoneSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customertype = CustomerTypeSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = CustomerPhone
        fields = [
            'customerphone_id','phone','customer','customertype','user','status','updated','created'
        ]

class CustomerAddressSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    customertype = CustomerTypeSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = CustomerAddress
        fields = [
            'customeraddress_id','address','city','province','postalcode',
            'customer','customertype','user','status','updated','created'
        ]
