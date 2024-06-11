from django.urls import path
from .views import CollateralEmployeeList, CollateralEmployeeDetail, GetSalaryCollateralByLoanID
# employeesbyloanid
urlpatterns = [
    path('employees/', CollateralEmployeeList.as_view(), name='employee-list'),
    path('employees/<int:pk>/', CollateralEmployeeDetail.as_view(), name='employee-detail'),
    path('employeesbyloanid/<int:loan>/', GetSalaryCollateralByLoanID.as_view(), name='byloanid-detail'),
]
