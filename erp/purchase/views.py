# views
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Requisition, RequisitionItem, PurchaseOrder
from .serializers import (
    RequisitionSerializer,
    PurchaseOrderSerializer,
    RequisitionItemSerializer
)
from django.shortcuts import get_object_or_404

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



class PurchaseOrderListView(generics.ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderListView(generics.ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class RequisitionItemCreateView(generics.CreateAPIView):
    queryset = RequisitionItem.objects.all()
    serializer_class = RequisitionItemSerializer

class RequisitionItemListView(generics.ListAPIView):
    queryset = RequisitionItem.objects.all()
    serializer_class = RequisitionItemSerializer