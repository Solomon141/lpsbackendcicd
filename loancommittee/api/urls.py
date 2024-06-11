from django.urls import path
from .views import LoanCommitteeList, LoanCommitteeDetail, ActiveCommittee

urlpatterns = [
    path('committee/', LoanCommitteeList.as_view() ),
    path('committee/<int:pk>', LoanCommitteeDetail.as_view()),
    path('active/', ActiveCommittee.as_view()),
]
