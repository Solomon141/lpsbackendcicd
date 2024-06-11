from django.urls import path
# from .views import ClientAccountViewWithID, GetClientByID
from .views import GetClientByExternalID
from .views import UserDetail, CustomerAllSavings
from .views import GetClientLoanPlan

# userdetail === allsaving

urlpatterns = [
    path('clientbyexternalid', GetClientByExternalID),
    path('userdetail', UserDetail ), 
    path('allsaving', CustomerAllSavings), 
    path('clientloanplan', GetClientLoanPlan), 
    
]
