"""
URL configuration for erp project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/user/', include('user.urls')),
    path('api/suppliers/', include('supplier.urls')),
    path('api/purchase-orders/', include('purchase.urls')),
    path('api/procurements/', include('procurement.urls')),
    path('api/projects/', include('project.urls')),
]
