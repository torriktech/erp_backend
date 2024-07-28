"""purchase order urls """
from django.urls import path
from .views import (
    RequisitionCreateView,
    RequisitionApproveView,
    PurchaseOrderListView,
    RequisitionItemCreateView,
    RequisitionItemListView
)

urlpatterns = [
    path('requisitions/',
         RequisitionCreateView.as_view(),
         name='requisition-create'),
    path('requisitions/<int:requisition_id>/approve/',
         RequisitionApproveView.as_view(),
         name='requisition-approve'),
    path('purchase-orders/',
         PurchaseOrderListView.as_view(),
         name='purchase-order-list'),
    path('requisition-items/',
         RequisitionItemCreateView.as_view(),
         name='requisition-item-create'),
    path('requisition-items/list/',
         RequisitionItemListView.as_view(),
         name='requisition-item-list'),
]
