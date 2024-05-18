'''purchase serializers'''
from rest_framework import serializers
from .models import (
    PurchaseOrder,
    Approval,
    Delivery,
    Invoice,
    QualityControl,
    Contract,
    Documentation
)


class PurchaseOrderSerializer(serializers.ModelSerializer):
    """
    Serializer for PurchaseOrder model.
    Provides serialization and deserialization of PurchaseOrder instances.

    Fields:
    - All fields from the PurchaseOrder model.
    """

    class Meta:
        """Purchase Order Meta"""
        model = PurchaseOrder
        fields = '__all__'


class ApprovalSerializer(serializers.ModelSerializer):
    """
    Serializer for Approval model.

    Provides serialization and deserialization of Approval instances.
    
    Fields:
    - All fields from the Approval model.
    """

    class Meta:
        """Approval Meta Class"""
        model = Approval
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    """
    Serializer for Delivery model.

    Provides serialization and deserialization of Delivery instances.
    
    Fields:
    - All fields from the Delivery model.
    """

    class Meta:
        """Delivery Meta class"""
        model = Delivery
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    """
    Serializer for Invoice model.

    Provides serialization and deserialization of Invoice instances.
    
    Fields:
    - All fields from the Invoice model.
    """

    class Meta:
        """Invoice Meta class"""
        model = Invoice
        fields = '__all__'


class QualityControlSerializer(serializers.ModelSerializer):
    """
    Serializer for QualityControl model.

    Provides serialization and deserialization of QualityControl instances.
    
    Fields:
    - All fields from the QualityControl model.
    """

    class Meta:
        """Quality Control Meta class"""
        model = QualityControl
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    """
    Serializer for Contract model.

    Provides serialization and deserialization of Contract instances.
    
    Fields:
    - All fields from the Contract model.
    """

    class Meta:
        """Contract Meta class"""
        model = Contract
        fields = '__all__'


class DocumentationSerializer(serializers.ModelSerializer):
    """
    Serializer for Documentation model.

    Provides serialization and deserialization of Documentation instances.
    
    Fields:
    - All fields from the Documentation model.
    """

    class Meta:
        """documentation Meta class"""
        model = Documentation
        fields = '__all__'