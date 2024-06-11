from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from holidays.api import views

urlpatterns = [
    path('holidays', views.Holidayviews.as_view()),
    path('holidays/<int:pk>', views.Holidaydetailviews.as_view()),
    path('holidays/bulkinsert', views.BulkInsertHoliday.as_view()),
    
]

# urlpatterns = format_suffix_patterns(urlpatterns)