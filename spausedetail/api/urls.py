from django.urls import path
from . import views

urlpatterns = [
    path('detail/', views.SpauseDetailList.as_view()),
    path('detail/<int:pk>/', views.SpauseDetailDetail.as_view()),
    path('spausebyparent/<int:parent>', views.GetSpauseDetailParentID.as_view()),
]
