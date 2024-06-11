from django.urls import path
from .views import LoanTypeListCreateAPIView, LoanTypeDetailAPIView, BulkInsertModel

urlpatterns = [
    path('loantypes/', LoanTypeListCreateAPIView.as_view(), name='loan-type-list-create'),
    path('loantypes/<int:pk>/', LoanTypeDetailAPIView.as_view(), name='loan-type-detail'),
    path('loantypes/bulkinsert', BulkInsertModel.as_view(), name='hometype-bulk'),
]
