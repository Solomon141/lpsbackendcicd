from django.urls import path
from .views import SubcityList, SubcityDetail, BulkInsertSubcity

urlpatterns = [
    path('subcitys/', SubcityList.as_view(), name='Subcity-list'),
    path('subcitys/<int:pk>/', SubcityDetail.as_view(), name='Subcity-detail'),
    path('subcitys/bulkinsert', BulkInsertSubcity.as_view()),
]
