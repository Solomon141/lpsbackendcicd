from django.urls import path
from .views import LoanGuaranteePersonFilesList, LoanGuaranteePersonFilesDetail

urlpatterns = [
    path('loan-guarantee-person-files/', LoanGuaranteePersonFilesList.as_view(), name='loan-guarantee-person-files-list'),
    path('loan-guarantee-person-files/<int:pk>/', LoanGuaranteePersonFilesDetail.as_view(), name='loan-guarantee-person-files-detail'),
]
