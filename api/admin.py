from django.contrib import admin

from api.models import (
    Customer,
    CustomerAddress,
    CustomerEmail,
    CustomerPhone,
    CustomerType,
    Status,
)


# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ['status_id', 'description']

admin.site.register(Status,StatusAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'firstname','lastname']

admin.site.register(Customer,CustomerAdmin)

class CustomerTypeAdmin(admin.ModelAdmin):
    list_display = ['customertype_id', 'description']

admin.site.register(CustomerType,CustomerTypeAdmin)

class CustomerPhoneAdmin(admin.ModelAdmin):
    list_display = ['customerphone_id', 'phone']

admin.site.register(CustomerPhone,CustomerPhoneAdmin)

class CustomerEmailAdmin(admin.ModelAdmin):
    list_display = ['customeremail_id', 'email']

admin.site.register(CustomerEmail,CustomerEmailAdmin)

class CustomerAddressAdmin(admin.ModelAdmin):
    list_display = ['customeraddress_id', 'address', 'city', 'province', 'postalcode']

admin.site.register(CustomerAddress,CustomerAddressAdmin)