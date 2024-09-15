# views
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Requisition, PurchaseOrder
from .serializers import (
    RequisitionSerializer,
    PurchaseOrderSerializer,
    # RequisitionItemSerializer
)
from django.shortcuts import get_object_or_404


class PurchaseOrderListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseOrderDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            order = PurchaseOrder.objects.get(pk=pk)
        except PurchaseOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PurchaseOrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        try:
            order = PurchaseOrder.objects.get(pk=pk)
        except PurchaseOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PurchaseOrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        try:
            order = PurchaseOrder.objects.get(pk=pk)
        except PurchaseOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class RequisitionCreateView(generics.CreateAPIView):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer


class RequisitionApproveView(APIView):

    def post(self, request, requisition_id):
        requisition = get_object_or_404(Requisition, id=requisition_id)
        if requisition.approvalStatus == 1:
            return Response({"detail": "Requisition already approved"}, status=status.HTTP_400_BAD_REQUEST)

        requisition.approvalStatus = 1  # Assuming 1 means approved
        requisition.approveby = request.user.username
        requisition.save()

        purchase_order_data = {
            'requisition': requisition.id,
            'order_date': request.data.get('order_date'),
            'delivery_date': request.data.get('delivery_date'),
            'payment_terms': request.data.get('payment_terms'),
            'payment_due_date': request.data.get('payment_due_date'),
            'shipping_method': request.data.get('shipping_method'),
            'delivery_address': request.data.get('delivery_address'),
            'approved_by': request.user.id
        }
        serializer = PurchaseOrderSerializer(data=purchase_order_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class RequisitionListView(generics.ListAPIView):
    """
    API View to retrieve all requisitions 
    with their items using Django Rest Framework's generic ListAPIView.
    """
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer


class RequisitionDetailView(generics.RetrieveAPIView):
    """View to retrieve a Requisition and its associated items"""
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer
    lookup_field = 'id'  # Look up requisition by ID

    def get(self, request, *args, **kwargs):
        try:
            requisition = self.get_object()  # Get the requisition by ID
            serializer = RequisitionSerializer(requisition)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Requisition.DoesNotExist:
            return Response(
                {"detail": "Requisition not found."},
                status=status.HTTP_404_NOT_FOUND
            )
