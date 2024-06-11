from django.urls import path
from .views import CollateralEmployeeFilesList, CollateralEmployeeFilesDetail, BulkInsert

urlpatterns = [
    path('employeefiles/', CollateralEmployeeFilesList.as_view(), name='employeefiles-list'),
    path('employeefiles/<int:pk>/', CollateralEmployeeFilesDetail.as_view(), name='employeefile-detail'),
    path('employeefiles/bulkinsert', BulkInsert.as_view()),
]
