from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hr/', include('HR.urls')),
    path('itDepartment/',include('ItDepartment.urls')),
    path('marketting/', include('Marketting.urls')),
    path('production/', include('Production.urls')),
    path('sales/', include('Sales.urls')),
    path('sd_st/',include('SD_ST.urls')),
    path('supplychain/', include('Supplychain.urls')),
    path('support/', include('Support.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
