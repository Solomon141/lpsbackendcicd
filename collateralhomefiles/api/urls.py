from django.urls import path
from .views import CollateralHomeFilesList, CollateralHomeFilesDetail, BulkInsert

urlpatterns = [
    path('homefiles', CollateralHomeFilesList.as_view(), name='homefiles-list'),
    path('homefiles/<int:pk>', CollateralHomeFilesDetail.as_view(), name='homefiles-detail'),
    path('homefiles/bulkinsert', BulkInsert.as_view()),
    
]
