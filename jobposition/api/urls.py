from django.urls import path
from .views import JonbPositionList, JonbPositionDetail

urlpatterns = [
    path('jobposition/', JonbPositionList.as_view() ),
    path('jobposition/<int:pk>/', JonbPositionDetail.as_view() ),
]
