from django.urls import path
from .views import CollateralHomeList, CollateralHomeDetail

urlpatterns = [
    path('collateralhomes/', CollateralHomeList.as_view(), name='collateralhome-list'),
    path('collateralhomes/<int:pk>/', CollateralHomeDetail.as_view(), name='collateralhome-detail'),
]
