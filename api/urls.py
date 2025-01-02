from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# from . import views
from api.viewsets.viewsets import (
    CustomerAddressViewSet,
    CustomerEmailViewSet,
    CustomerPhoneViewSet,
    CustomerTypeViewSet,
    CustomerViewSet,
    StatusViewSet,
    UserViewSet,
)

# routers
router = DefaultRouter()
# Status
router.register('v1/status', StatusViewSet)
# CustomerType
router.register('v1/customertype', CustomerTypeViewSet)
# Users
router.register('v1/users', UserViewSet)
# Customer
router.register('v1/customer', CustomerViewSet)
# Customer Email
router.register('v1/customeremail', CustomerEmailViewSet)
# Customer Phone
router.register('v1/customerphone', CustomerPhoneViewSet)
# Customer Address
router.register('v1/customeraddress', CustomerAddressViewSet)

urlpatterns =[ 
    # JWT Authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Users
    # path('v1/users/', views.UserList.as_view(), name='user-list'),
    # path('v1/users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    # # Statuses
    # path('v1/status/', views.StatusList.as_view(), name='status-list'),
    # path('v1/status/<int:pk>/', views.StatusDetail.as_view(), name='status-detail'),
    # Customers
    # path('v1/customers/', views.CustomerList.as_view(), name='customer-list'),
    # path('v1/customers/<int:pk>/', views.CustomerDetail.as_view(), name='customer-detail'),
    # # Customer Types
    # path('v1/customertype/', views.CustomerTypeList.as_view(), name='customertype-list'),
    # path('v1/customertype/<int:pk>/', views.CustomerTypeDetail.as_view(), name='customertype-detail'),
    # Customer Email
    # path('v1/customeremail/', views.CustomerEmailList.as_view(), name='customeremail-list'),
    # path('v1/customeremail/<int:pk>/', views.CustomerEmailDetail.as_view(), name='customeremail-detail'),
    # Customer Phone
    # path('v1/customerphone/', views.CustomerPhoneList.as_view(), name='customerphone-list'),
    # path('v1/customerphone/<int:pk>/', views.CustomerPhoneDetail.as_view(), name='customerphone-detail'),
    # # Customer Address
    # path('v1/customeraddress/', views.CustomerAddressList.as_view(), name='customeraddress-list'),
    # path('v1/customeraddress/<int:pk>/', views.CustomerAddressDetail.as_view(), name='customeraddress-detail'), 
 ]

# Include the router URLs in our URL configuration.
urlpatterns += router.urls