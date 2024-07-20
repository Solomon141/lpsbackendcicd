from django.urls import path
from .views import WithdrawalDetail, WithdrawalList, WithdrawByExternalID

urlpatterns = [
    path('withdrawal/', WithdrawalList.as_view(), name='withdrawal-list'),
    path('withdrawal/<str:pk>/', WithdrawalDetail.as_view(), name='withdrawal-detail'),
    path('withexternalId/<int:externalId>', WithdrawByExternalID.as_view()),
]
