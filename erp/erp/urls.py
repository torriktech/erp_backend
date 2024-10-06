"""
URL configuration for erp project.
"""
from django.contrib import admin
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/admin/', admin.site.urls),
    # path('api/auths/login/',
    #      TokenObtainPairView.as_view(),
    #      name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    path('api/auths/', include('auths.urls')),
    path('api/clients/', include('clients.urls')),
    path('api/suppliers/', include('supplier.urls')),
    path('api/categories/', include('category.urls')),
    path('api/items/', include('items.urls')),
    path('api/cashbooks/', include('cashbook.urls')),
    path('api/departments/', include('departments.urls')),

    path('api/purchase/', include('purchase.urls')),
    path('api/projects/', include('project.urls')),
    path('api/boq/', include('bill_of_quantity.urls')),

    # budget routes
    path('api/budgets/', include('budget.urls')),
    # payroll and appraisal route
    path('api/payrolls/', include('payroll.urls')),
]
