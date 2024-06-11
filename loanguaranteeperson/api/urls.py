from django.urls import path
from .views import LoanGuaranteePersonList, LoanGuaranteePersonDetail, GetGuaranteePersonByLoanID

urlpatterns = [
    path('loan-guarantee-persons/', LoanGuaranteePersonList.as_view()),
    path('loan-guarantee-persons/<int:pk>/', LoanGuaranteePersonDetail.as_view()),
    path('loan-gp-byloan/<int:loan>/', GetGuaranteePersonByLoanID.as_view()),
]
