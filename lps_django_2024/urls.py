"""
URL configuration for lps_django_2024 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="AMIGOSSACCO - Loan Processing System (LPS) API",
        default_version='v1',
        description="An api for contacts",
        terms_of_service="https://fiab-real-estate.vercel.app/terms",
        contact=openapi.Contact(email="weymit2001@gmail.com"),
        license=openapi.License(name="LPS License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include("debug_toolbar.urls")),
    path('lpsauth/', include('authentication.api.urls')),
    path('employeedetail/', include('employeedetail.api.urls')),

    # fineract
    path("fineract/", include('fineract.api.urls')),

    # # lookups
    path('checklist/', include('checklist.api.urls')),
    path('checklist_type/', include('checklisttype.api.urls')),
    path('subcity/', include('subcity.api.urls')),
    path('woreda/', include('woreda.api.urls')),
    path('loantype/', include('loantype.api.urls')),


    # # customer
    path('customer/', include('customer.api.urls')),
    path('customer_married/', include('customermarried.api.urls')),
    path('customer_single/', include('customersingle.api.urls')),
    path('spause/', include('spausedetail.api.urls')),
    

    # # loan
    path('loan/', include('loan.api.urls')),
    path('loan_comment/', include('loancomment.api.urls')),
    path('loan_delegation_person/', include('delegation.api.urls')),
    path('loan_guarantee_person/', include('loanguaranteeperson.api.urls')),
    path('loan_guarantee_person_files/', include('loanguaranteepersonfiles.api.urls')),
    path('surety/', include('surety.api.urls')),
    path('loanwitness/', include('loanwitness.api.urls')),
    path('loanadditionaldocs/', include('loanadditionaldocs.api.urls')),



    # # collateral Car Collateral
    path('collateral_car/', include('collateralcar.api.urls')),
    path('collateral_stock/', include('collateralstock.api.urls')),
    path('collateral_stock_files/', include('collateralstockfiles.api.urls')),
    
    path('car_model/', include('carmodel.api.urls')),
    path('car_commonfiles/', include('carcommonfiles.api.urls')),
    path('car_garagevalue/', include('cargaragevalue.api.urls')),
    path('car_manufacturer/', include('carmanufacturer.api.urls')),
    path('car_marketvalue/', include('carmarketvalue.api.urls')),

    # # collateral Home Collateral
    path('collateral_home/', include('collateralhome.api.urls')),
    path('home_type/', include('hometype.api.urls')),
    path('home_commonfiles/', include('collateralhomefiles.api.urls')),

    # collateralemployee
    path('collateral_employee/', include('collateralemployee.api.urls')),
    path('collateral_employee_files/', include('collateralemployeefiles.api.urls')),
    path('holidays/', include('holidays.api.urls')),
    
    # loanguaranteepersonfiles
    path('loan_guaranteeperson_files/', include('loanguaranteepersonfiles.api.urls')),
    path('loancommittee/', include('loancommittee.api.urls')),
    path('jobposition/', include('jobposition.api.urls')),
    path('customercommonfiles/', include('customercommonfiles.api.urls')),
    
    # disbursements
    path('disbursements/', include('disbursement.api.urls')),
    
    
    

    path('newlps/', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path("redoc", schema_view.with_ui('redoc',
                                      cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)