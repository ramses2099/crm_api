from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Status(models.Model):
    status_id = models.BigAutoField(primary_key=True,
                                       auto_created=True,
                                       serialize=False,
                                       verbose_name="status_id"
                                       )
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, related_name="status", on_delete=models.PROTECT)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{status_id:%d, description:%s}" % (self.status_id,self.description)
    
class CustomerType(models.Model):
    customertype_id = models.BigAutoField(primary_key=True,
                                       auto_created=True,
                                       serialize=False,
                                       verbose_name="customertype_id"
                                       )
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, related_name="user", on_delete=models.PROTECT)
    status = models.ForeignKey(Status, related_name="status", on_delete=models.PROTECT)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.description

class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True,
                                       auto_created=True,
                                       serialize=False,
                                       verbose_name="customer_id"
                                       )
    firstname = models.CharField(max_length=600)
    lastname = models.CharField(max_length=600)
    customertype = models.ForeignKey(CustomerType, on_delete=models.PROTECT)    
    user = models.ForeignKey(User, related_name="users", on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
    
class CustomerEmail(models.Model):
    customeremail_id = models.BigAutoField(primary_key=True,
                                       auto_created=True,
                                       serialize=False,
                                       verbose_name="customeremail_id"
                                       )
    email = models.EmailField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    customertype = models.ForeignKey(CustomerType, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.email

class CustomerPhone(models.Model):
    customerphone_id = models.BigAutoField(primary_key=True,
                                       auto_created=True,
                                       serialize=False,
                                       verbose_name="customerphone_id"
                                       )
    phone = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    customertype = models.ForeignKey(CustomerType, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.phone
    
class CustomerAddress(models.Model):
    customeraddress_id = models.BigAutoField(primary_key=True,
                                       auto_created=True,
                                       serialize=False,
                                       verbose_name="customeraddress_id"
                                       )
    address = models.CharField(max_length=850)
    city  = models.CharField(max_length=500)
    province  = models.CharField(max_length=500)
    postalcode  = models.CharField(max_length=15)    
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    customertype = models.ForeignKey(CustomerType, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.address
    
