"""purchase order urls """
from django.urls import path
from .views import (
    RequisitionCreateView,
    RequisitionApproveView,
    PurchaseOrderDetailView,
    PurchaseOrderListCreateView,
    PurchaseOrderListCreateView,
    RequisitionListView,
    RequisitionDetailView
)


urlpatterns = [
    path('purchase-orders/', PurchaseOrderListCreateView.as_view(),
         name='purchase-order-list-create'),
    path('purchase-orders/<int:pk>/',
         PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('requisitions/list/', RequisitionListView.as_view(), name='requisition-list'),
    path('requisitions/',
         RequisitionCreateView.as_view(),
         name='requisition-create'),
    path('requisitions/<int:requisition_id>/approve/',
         RequisitionApproveView.as_view(),
         name='requisition-approve'),
    path('requisition/<int:id>/', RequisitionDetailView.as_view(),
         name='requisition-detail'),
]
