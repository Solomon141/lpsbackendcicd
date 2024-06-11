from django.urls import path
from .views import CarManufactureList, CarManufactureDetail, BulkInsertManufacture

urlpatterns = [
    path('carmanufacture/', CarManufactureList.as_view(), name='carmanufacture-list'),
    path('carmanufacture/<int:pk>/', CarManufactureDetail.as_view(), name='carmanufacture-detail'),
    path('manufacture/bulkinsert', BulkInsertManufacture.as_view()),

]
