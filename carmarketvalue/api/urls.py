from django.urls import path
from .views import CarMarketValueList, CarMarketValueDetail

urlpatterns = [
    path('carmarketvalues/', CarMarketValueList.as_view(), name='carmarketvalue-list'),
    path('carmarketvalues/<int:pk>/', CarMarketValueDetail.as_view(), name='carmarketvalue-detail'),
]
