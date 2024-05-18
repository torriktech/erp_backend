from rest_framework import serializers
from .models import Procurement
from supplier.serializers import SupplierSerializer
from purchase.serializers import PurchaseOrderSerializer, DocumentationSerializer

class ProcurementSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    purchase_order = PurchaseOrderSerializer()
    documentation = DocumentationSerializer()

    class Meta:
        model = Procurement
        fields = '__all__'
