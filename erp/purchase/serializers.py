'''purchase serializers'''
from rest_framework import serializers
from items.serializers import ItemSerializer
from .models import (
    Requisition,
    RequisitionItem,
    PurchaseOrder
)


class RequisitionItemSerializer(serializers.ModelSerializer):
    """requisition item serializer"""
    item = ItemSerializer()

    class Meta:
        """meta data"""
        model = RequisitionItem
        fields = '__all__'


class RequisitionSerializer(serializers.ModelSerializer):
    """requisition class"""
    items = RequisitionItemSerializer(many=True)

    class Meta:
        """additional data"""
        model = Requisition
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        requisition = Requisition.objects.create(**validated_data)
        for item_data in items_data:
            RequisitionItem.objects.create(
                requisition=requisition,
                **item_data)
        return requisition

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        instance.name = validated_data.get('name', instance.name)
        instance.project = validated_data.get('project', instance.project)
        instance.requested_by = validated_data.get('requested_by', instance.requested_by)
        instance.description = validated_data.get('description', instance.description)
        instance.schedule_date = validated_data.get('schedule_date', instance.schedule_date)
        instance.approval_status = validated_data.get('approval_status', instance.approval_status)
        instance.task = validated_data.get('task', instance.task)
        instance.approve_by = validated_data.get(
            'approve_by', instance.approve_by)
        instance.save()

        for item_data in items_data:
            item = RequisitionItem.objects.filter(
                requisition=instance,
                id=item_data['id']).first()
            if item:
                item.item = item_data.get('item', item.item)
                item.quantity = item_data.get('quantity', item.quantity)
                item.save()
            else:
                RequisitionItem.objects.create(
                    requisition=instance, **item_data)

        return instance


class PurchaseOrderSerializer(serializers.ModelSerializer):
    """purchase serializers"""
    class Meta:
        """meta data"""
        model = PurchaseOrder
        fields = '__all__'


# class ApprovalSerializer(serializers.ModelSerializer):
#     """
#     Serializer for Approval model.

#     Provides serialization and deserialization of Approval instances.
    
#     Fields:
#     - All fields from the Approval model.
#     """

#     class Meta:
#         """Approval Meta Class"""
#         model = Approval
#         fields = '__all__'


# class DeliverySerializer(serializers.ModelSerializer):
#     """
#     Serializer for Delivery model.

#     Provides serialization and deserialization of Delivery instances.
    
#     Fields:
#     - All fields from the Delivery model.
#     """

#     class Meta:
#         """Delivery Meta class"""
#         model = Delivery
#         fields = '__all__'


# class InvoiceSerializer(serializers.ModelSerializer):
#     """
#     Serializer for Invoice model.

#     Provides serialization and deserialization of Invoice instances.
    
#     Fields:
#     - All fields from the Invoice model.
#     """

#     class Meta:
#         """Invoice Meta class"""
#         model = Invoice
#         fields = '__all__'


# class QualityControlSerializer(serializers.ModelSerializer):
#     """
#     Serializer for QualityControl model.

#     Provides serialization and deserialization of QualityControl instances.
    
#     Fields:
#     - All fields from the QualityControl model.
#     """

#     class Meta:
#         """Quality Control Meta class"""
#         model = QualityControl
#         fields = '__all__'


# class ContractSerializer(serializers.ModelSerializer):
#     """
#     Serializer for Contract model.

#     Provides serialization and deserialization of Contract instances.
    
#     Fields:
#     - All fields from the Contract model.
#     """

#     class Meta:
#         """Contract Meta class"""
#         model = Contract
#         fields = '__all__'


# class DocumentationSerializer(serializers.ModelSerializer):
#     """
#     Serializer for Documentation model.

#     Provides serialization and deserialization of Documentation instances.
    
#     Fields:
#     - All fields from the Documentation model.
#     """

#     class Meta:
#         """documentation Meta class"""
#         model = Documentation
#         fields = '__all__'