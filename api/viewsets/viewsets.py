from django.contrib.auth.models import User
from rest_framework import viewsets

from api.models import (
    Customer,
    CustomerAddress,
    CustomerEmail,
    CustomerPhone,
    CustomerType,
    Status,
)
from api.serializers import (
    CustomerAddressSerializer,
    CustomerEmailSerializer,
    CustomerPhoneSerializer,
    CustomerSerializer,
    CustomerTypeSerializer,
    StatusSerializer,
    UserSerializer,
)


# Viewset classes
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
   
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerTypeViewSet(viewsets.ModelViewSet):
    queryset = CustomerType.objects.all()
    serializer_class = CustomerTypeSerializer

class CustomerEmailViewSet(viewsets.ModelViewSet):
    queryset = CustomerEmail.objects.all()
    serializer_class = CustomerEmailSerializer

class CustomerPhoneViewSet(viewsets.ModelViewSet):
    queryset = CustomerPhone.objects.all()
    serializer_class = CustomerPhoneSerializer

class CustomerAddressViewSet(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer

