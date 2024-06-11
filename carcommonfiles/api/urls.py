from django.urls import path
from .views import CarFilesList, CarFilesDetail, BulkInsert

urlpatterns = [
    path('carfiles', CarFilesList.as_view(), name='carfiles-list'),
    path('carfiles/<int:pk>', CarFilesDetail.as_view(), name='carfiles-detail'),
    path('carfiles/bulkinsert', BulkInsert.as_view()),
    
]
