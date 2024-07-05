from django.urls import path
from .views import DisbursementList, DisbursementDetail

urlpatterns = [
    path('disbursements/', DisbursementList.as_view(), name='Disbursement-list'),
    path('disbursements/<int:pk>/', DisbursementDetail.as_view(), name='Disbursement-detail'),
]
