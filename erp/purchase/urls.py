"""purchase order urls """
from django.urls import path
from .views import (
    PurchaseOrderListCreateAPIView,
    PurchaseOrderDetailAPIView,
    ApprovalDetailAPIView,
    DeliveryDetailAPIView,
    InvoiceDetailAPIView,
    QualityControlDetailAPIView,
    ContractDetailAPIView,
    DocumentationDetailAPIView
)

urlpatterns = [
    path('purchase-orders/',
         PurchaseOrderListCreateAPIView.as_view(),
         name='purchaseorder-list-create'),
    path('purchase-orders/<int:pk>/',
         PurchaseOrderDetailAPIView.as_view(),
         name='purchaseorder-detail'),

    path('approvals/<int:pk>/',
         ApprovalDetailAPIView.as_view(),
         name='approval-detail'),
    path('deliveries/<int:pk>/',
         DeliveryDetailAPIView.as_view(),
         name='delivery-detail'),
    path('invoices/<int:pk>/',
         InvoiceDetailAPIView.as_view(),
         name='invoice-detail'),
    path('quality-controls/<int:pk>/',
         QualityControlDetailAPIView.as_view(),
         name='qualitycontrol-detail'
         ),
    path('contracts/<int:pk>/',
         ContractDetailAPIView.as_view(),
         name='contract-detail'
         ),
    path('documentations/<int:pk>/',
         DocumentationDetailAPIView.as_view(),
         name='documentation-detail'),
]
