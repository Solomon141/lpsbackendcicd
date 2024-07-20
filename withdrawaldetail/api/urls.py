from django.urls import path
from .views import WithdrawalDetailDetail, WithdrawalDetailList

urlpatterns = [
    path('withdrawaldetail/', WithdrawalDetailList.as_view(), name='withdrawaldetail-list'),
    path('withdrawaldetail/<int:pk>/', WithdrawalDetailDetail.as_view(), name='withdrawaldetail-detail'),
]
