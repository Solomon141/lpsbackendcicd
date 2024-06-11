from django.urls import path
from .views import WoredaView, WoredaDetail, BulkInsertCkeckList
from .views import GetWoredaByParentID

urlpatterns = [
    path('woredas/', WoredaView.as_view(), name='Woreda-list'),
    path('woredas/<int:pk>/', WoredaDetail.as_view(), name='Woreda-detail'),
    path('woredas/bulkinsert', BulkInsertCkeckList.as_view()),
    path('woredabyparent/<int:parent>', GetWoredaByParentID.as_view()),
]
