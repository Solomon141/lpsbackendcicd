from django.urls import path
from .views import CustommerSingleList, CustommerSingleDetail, BulkInsert

urlpatterns = [
    path('custommersingle/', CustommerSingleList.as_view(), name='custommerSingle-list'),
    path('custommersingle/<int:pk>/', CustommerSingleDetail.as_view(), name='custommerSingle-detail'),
    path('custommersingle/bulkinsert', BulkInsert.as_view()),
]
