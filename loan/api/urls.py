from django.urls import path
from .views import LoanList, LoanDetail

urlpatterns = [
    path('loans/', LoanList.as_view(), name='loan-list'),
    path('loans/<int:pk>/', LoanDetail.as_view(), name='loan-detail'),
]
