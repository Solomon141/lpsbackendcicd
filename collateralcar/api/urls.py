from django.urls import path
from .views import CollateralCarList, CollateralCarDetail

urlpatterns = [
    path('collateralcar/', CollateralCarList.as_view(), name='collateralcar-list'),
    path('collateralcar/<int:pk>/', CollateralCarDetail.as_view(), name='collateralcar-detail'),
]
