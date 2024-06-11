from django.urls import path
from .views import CollateralStockFilesList, CollateralStockFilesDetail, BulkInsert

urlpatterns = [
    path('stockfiles/', CollateralStockFilesList.as_view(), name='stockfiles-list'),
    path('stockfiles/<int:pk>/', CollateralStockFilesDetail.as_view(), name='stockfile-detail'),
    path('stockfiles/bulkinsert', BulkInsert.as_view()),
]
