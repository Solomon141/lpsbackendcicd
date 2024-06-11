from django.urls import path
from .views import CustomerList, CustomerDetail, GetUserByExternalID, GetUserByFineractCustID

urlpatterns = [
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    path('clientbyexternalid/<str:entityExternalId>', GetUserByExternalID.as_view()),
    path('clientbyaccountnumber/<str:entityAccountNo>', GetUserByFineractCustID.as_view()),
]
