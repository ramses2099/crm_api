from django.urls import path

from . import views

urlpatterns =[    
    # Users
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    # Statuses
    path('status/', views.StatusList.as_view(), name='status-list'),
    path('status/<int:pk>/', views.StatusDetail.as_view(), name='status-detail'),
    # Customers
    path('customers/', views.CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetail.as_view(), name='customer-detail'),
    # Customer Types
    path('customertype/', views.CustomerTypeList.as_view(), name='customertype-list'),
    path('customertype/<int:pk>/', views.CustomerTypeDetail.as_view(), name='customertype-detail'),
    # Customer Email
    path('customeremail/', views.CustomerEmailList.as_view(), name='customeremail-list'),
    path('customeremail/<int:pk>/', views.CustomerEmailDetail.as_view(), name='customeremail-detail'),
    # Customer Phone
    path('customerphone/', views.CustomerPhoneList.as_view(), name='customerphone-list'),
    path('customerphone/<int:pk>/', views.CustomerPhoneDetail.as_view(), name='customerphone-detail'),
    # Customer Address
    path('customeraddress/', views.CustomerAddressList.as_view(), name='customeraddress-list'),
    path('customeraddress/<int:pk>/', views.CustomerAddressDetail.as_view(), name='customeraddress-detail'),
 
 ]