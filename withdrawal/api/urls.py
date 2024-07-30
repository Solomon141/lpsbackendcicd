from django.urls import path
from .views import WithdrawalDetail, WithdrawalList, WithdrawByCustomerID, BulkInsertWithdrawal

urlpatterns = [
    path('withdrawal/', WithdrawalList.as_view(), name='withdrawal-list'),
    path('withdrawal/<str:pk>/', WithdrawalDetail.as_view(), name='withdrawal-detail'),
    path('withcustomerId/<str:customerId>', WithdrawByCustomerID.as_view()),
    path('withdrawal/bulkinsert', BulkInsertWithdrawal.as_view()),
]
