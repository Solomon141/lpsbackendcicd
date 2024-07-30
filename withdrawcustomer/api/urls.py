from django.urls import path
from .views import WithdrawCustomerList, WithdrawCustomerDetail, GetUserByExternalID, GetUserByFineractCustID

urlpatterns = [
    path('withdrawcustomers/', WithdrawCustomerList.as_view(), name='Withdrawcustomer-list'),
    path('withdrawcustomers/<str:pk>/', WithdrawCustomerDetail.as_view(), name='Withdrawcustomer-detail'),
    path('clientbyexternalid/<str:entityExternalId>', GetUserByExternalID.as_view()),
    path('clientbyaccountnumber/<str:entityAccountNo>', GetUserByFineractCustID.as_view()),
]
