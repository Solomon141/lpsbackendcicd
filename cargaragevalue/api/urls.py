from django.urls import path
from .views import GarageReportList, GarageReportDetail

urlpatterns = [
    path('garagereports/', GarageReportList.as_view(), name='garagereport-list'),
    path('garagereports/<int:pk>/', GarageReportDetail.as_view(), name='garagereport-detail'),
]
