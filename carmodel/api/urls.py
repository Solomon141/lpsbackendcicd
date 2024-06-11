from django.urls import path
from .views import CarModelList, CarModelDetail, BulkInsertModel

urlpatterns = [
    path('cars/', CarModelList.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarModelDetail.as_view(), name='car-detail'),
    path('model/bulkinsert', BulkInsertModel.as_view()),

]
