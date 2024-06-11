from django.urls import path
from .views import HomeTypeList, HomeTypeDetail, BulkInsertModel

urlpatterns = [
    path('hometypes/', HomeTypeList.as_view(), name='hometype-list'),
    path('hometypes/<int:pk>', HomeTypeDetail.as_view(), name='hometype-detail'),
    path('hometypes/bulkinsert', BulkInsertModel.as_view(), name='hometype-bulk'),
]
