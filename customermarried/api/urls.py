from django.urls import path
from .views import CustommerMarriedList, CustommerMarriedDetail, BulkInsert

urlpatterns = [
    path('custommermarried/', CustommerMarriedList.as_view(), name='custommermarried-list'),
    path('custommermarried/<int:pk>/', CustommerMarriedDetail.as_view(), name='custommermarried-detail'),
    path('custommermarried/bulkinsert', BulkInsert.as_view()),
]
