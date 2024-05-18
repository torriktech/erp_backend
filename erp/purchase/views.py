"""purchase order controller"""
from rest_framework import generics
from .models import (
    PurchaseOrder,
    Approval,
    Delivery,
    Invoice, 
    QualityControl,
    Contract,
    Documentation
)
from .serializers import (
    PurchaseOrderSerializer,
    ApprovalSerializer,
    DeliverySerializer,
    InvoiceSerializer,
    QualityControlSerializer,
    ContractSerializer,
    DocumentationSerializer
)


class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing and creating PurchaseOrder instances.

    - Lists all PurchaseOrder instances.
    - Creates a new PurchaseOrder instance.
    """
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a PurchaseOrder instance.

    - Retrieves a specific PurchaseOrder instance by its id.
    - Updates an existing PurchaseOrder instance.
    - Deletes an existing PurchaseOrder instance.
    """
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class ApprovalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting an Approval instance.

    - Retrieves a specific Approval instance by its id.
    - Updates an existing Approval instance.
    - Deletes an existing Approval instance.
    """
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer


class DeliveryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Delivery instance.

    - Retrieves a specific Delivery instance by its id.
    - Updates an existing Delivery instance.
    - Deletes an existing Delivery instance.
    """
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class InvoiceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting an Invoice instance.

    - Retrieves a specific Invoice instance by its id.
    - Updates an existing Invoice instance.
    - Deletes an existing Invoice instance.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class QualityControlDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a QualityControl instance.

    - Retrieves a specific QualityControl instance by its id.
    - Updates an existing QualityControl instance.
    - Deletes an existing QualityControl instance.
    """
    queryset = QualityControl.objects.all()
    serializer_class = QualityControlSerializer

class ContractDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Contract instance.

    - Retrieves a specific Contract instance by its id.
    - Updates an existing Contract instance.
    - Deletes an existing Contract instance.
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class DocumentationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a Documentation instance.

    - Retrieves a specific Documentation instance by its id.
    - Updates an existing Documentation instance.
    - Deletes an existing Documentation instance.
    """
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
