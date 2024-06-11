from django.urls import path
from .views import LoanAdditionalFilesList, LoanAdditionalFilesDetail, GetCheckListByParentID, BulkInsert

urlpatterns = [
    path('additionalfiles', LoanAdditionalFilesList.as_view() ),
    path('additionalfiles/<int:pk>', LoanAdditionalFilesDetail.as_view() ),
    path('additionalfilesbyparent/<int:parent>', GetCheckListByParentID.as_view() ),
    path('additionalfiles/bulkinsert', BulkInsert.as_view()),
]
