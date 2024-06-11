from django.urls import path
from .views import CollateralStockDetail, CollateralStockList, GetStockCollateralByLoanID

urlpatterns = [
    path('collateralstock/', CollateralStockList.as_view() ),
    path('collateralstock/<int:pk>/', CollateralStockDetail.as_view() ),
    path('stockbyloanid/<int:loan>/', GetStockCollateralByLoanID.as_view()),
]
