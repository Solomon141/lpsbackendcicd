from django.urls import path
from .views import CheckListView, CheckListDetail, BulkInsertCkeckList
from .views import GetCheckListByParentID

urlpatterns = [
    path('checklists/', CheckListView.as_view(), name='checklist-list'),
    path('checklists/<int:pk>/', CheckListDetail.as_view(), name='checklist-detail'),
    path('checklists/bulkinsert', BulkInsertCkeckList.as_view()),
    path('checklistbyparent/<int:parent>', GetCheckListByParentID.as_view()),
]
