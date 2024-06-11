from django.urls import path
from .views import CustomerCommonFilesList, CustomerCommonFilesDetail, GetCheckListByParentID, BulkInsert

urlpatterns = [
    path('commonfiles', CustomerCommonFilesList.as_view() ),
    path('commonfiles/<int:pk>', CustomerCommonFilesDetail.as_view() ),
    path('commonfilesbyparent/<int:parent>', GetCheckListByParentID.as_view() ),
    path('commonfiles/bulkinsert', BulkInsert.as_view()),
]
