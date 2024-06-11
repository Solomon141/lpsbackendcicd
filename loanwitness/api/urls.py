from django.urls import path
from .views import LoanWitnessList, LoanWitnessDetail, GetWitnessByLoanID

urlpatterns = [
    path('witness/', LoanWitnessList.as_view(), name='witness-list'),
    path('witness/<int:pk>/', LoanWitnessDetail.as_view(), name='witness-detail'),
    path('witnessbyloanid/<int:loan>/', GetWitnessByLoanID.as_view(), name='witness-detail'),
]
