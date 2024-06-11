from django.urls import path
from .views import SuretyList, SuretyDetail

urlpatterns = [
    path('sureties/', SuretyList.as_view(), name='surety-list'),
    path('sureties/<int:pk>/', SuretyDetail.as_view(), name='surety-detail'),
]
