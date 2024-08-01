from django.urls import path
from .views import (
    SupplierListView,
    SupplierCreateView,
    SupplierDetailView,
    SupplierUpdateView,
    SupplierDestroyView
)

urlpatterns = [
    path('', SupplierListView.as_view(), name='supplier-list'),
    path('create/', SupplierCreateView.as_view(), name='supplier-create'),
    path('detailed/<int:pk>/', SupplierDetailView.as_view(), name='supplier-detail'),
    path('update/<int:pk>/', SupplierUpdateView.as_view(), name='supplier-update'),
    path('delete/<int:pk>/', SupplierDestroyView.as_view(), name='supplier-delete'),
]


