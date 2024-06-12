from rest_framework import serializers
from .models import Procurement
from purchase.serializers import PurchaseOrderSerializer, DocumentationSerializer

class ProcurementSerializer(serializers.ModelSerializer):
    purchase_order = PurchaseOrderSerializer()
    documentation = DocumentationSerializer()

    class Meta:
        model = Procurement
        fields = '__all__'
