from django.urls import path
from .views import LoanCommentList, LoanCommentDetail

urlpatterns = [
    path('loancomments/', LoanCommentList.as_view(), name='loancomment-list'),
    path('loancomments/<int:pk>/', LoanCommentDetail.as_view(), name='loancomment-detail'),
]
