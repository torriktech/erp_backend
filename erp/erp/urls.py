"""
URL configuration for erp project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/auths/', include('auths.urls')),
    path('api/clients/', include('clients.urls')),
    path('api/suppliers/', include('supplier.urls')),
    path('api/items/', include('items.urls')),
    path('api/departments/', include('departments.urls')),

    path('api/purchase/', include('purchase.urls')),
    path('api/projects/', include('project.urls')),
    path('api/boq/', include('bill_of_quantity.urls')),

    # budget routes
    path('api/budgets/', include('budget.urls')),
    # payroll and appraisal route
    path('api/payrolls/', include('payroll.urls')),
]
