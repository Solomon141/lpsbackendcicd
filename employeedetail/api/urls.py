from django.urls import path
from .views import EmployeeDetailAPIView, EmployeeDetailDetailAPIView, EmployeeDetailUpsertAPIView

urlpatterns = [
    path('employees/', EmployeeDetailAPIView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailDetailAPIView.as_view(), name='employee-detail'),
    path('employee-upsert/', EmployeeDetailUpsertAPIView.as_view(), name='employee-upsert'),
]