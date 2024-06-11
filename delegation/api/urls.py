from django.urls import path
from .views import DelegationList, DelegationDetail, GetDelegationByLoanID

urlpatterns = [
    path('delegation/', DelegationList.as_view(), name='delegation-list'),
    path('delegation/<int:pk>/', DelegationDetail.as_view(), name='delegation-detail'),
    path('delegationbyloanid/<int:loan>/', GetDelegationByLoanID.as_view(), name='delegation-byloanid'),
]
