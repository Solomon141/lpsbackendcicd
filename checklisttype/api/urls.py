from django.urls import path
from .views import CheckListTypeList, CheckListTypeDetail, BulkInsertCheckListType

urlpatterns = [
    path('checklisttypes/', CheckListTypeList.as_view(), name='checklisttype-list'),
    path('checklisttypes/<int:pk>/', CheckListTypeDetail.as_view(), name='checklisttype-detail'),
    path('checklisttypes/bulkinsert', BulkInsertCheckListType.as_view()),

]
