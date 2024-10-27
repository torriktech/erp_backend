from rest_framework import serializers
from .models import Requisition, RequisitionItem, PurchaseOrder
from items.models import Item
from project.models import Project
from auths.models import Employee


class RequisitionItemSerializer(serializers.ModelSerializer):
    """Serializer for RequisitionItem"""
    item = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all())  # Assuming you want to send item ID

    class Meta:
        model = RequisitionItem
        fields = ['id', 'item', 'quantity', 'price']


class RequisitionSerializer(serializers.ModelSerializer):
    """Serializer for Requisition"""
    items = RequisitionItemSerializer(
        many=True)  # Use the RequisitionItemSerializer
# Use PrimaryKeyRelatedField for related models
    project = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all())
    requested_by = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), required=False)
    approve_by = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), required=False)

    class Meta:
        model = Requisition
        fields = ['id', 'name', 'project', 'complain', 'requested_by', 'description',
                  'schedule_date', 'approval_status', 'task', 'approve_by', 'items']

    def create(self, validated_data):
        # Remove `requested_by` from the data if it exists
        validated_data.pop('requested_by', None)
        
        # Get the currently logged-in user from the request context
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            try:
                employee = request.user.employee
                validated_data['requested_by'] = employee
            except Employee.DoesNotExist:
                raise serializers.ValidationError("Logged-in user is not associated with an employee record.")
        else:
            raise serializers.ValidationError("kindly login")

        items_data = validated_data.pop('items', [])
        # Create the requisition object
        requisition = Requisition.objects.create(**validated_data)

        # Create each RequisitionItem
        for item_data in items_data:
            item = item_data.pop('item')  # Retrieve the item instance
            print(item)
            RequisitionItem.objects.create(
                requisition=requisition, item=item, **item_data)

        return requisition

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', [])

        # Update the requisition fields
        instance.name = validated_data.get('name', instance.name)
        instance.project = validated_data.get('project', instance.project)
        instance.complain = validated_data.get('complain', instance.complain)
        instance.requested_by = validated_data.get(
            'requested_by', instance.requested_by)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.schedule_date = validated_data.get(
            'schedule_date', instance.schedule_date)
        instance.approval_status = validated_data.get(
            'approval_status', instance.approval_status)
        instance.task = validated_data.get('task', instance.task)
        instance.approve_by = validated_data.get(
            'approve_by', instance.approve_by)
        instance.save()

        # Update or create requisition items
        for item_data in items_data:
            item = item_data.pop('item')  # Retrieve the item instance
            req_item = RequisitionItem.objects.filter(
                requisition=instance, item=item).first()
            if req_item:
                req_item.quantity = item_data.get(
                    'quantity', req_item.quantity)
                req_item.price = item_data.get('price', req_item.price)
                req_item.save()
            else:
                RequisitionItem.objects.create(
                    requisition=instance, item=item, **item_data)

        return instance



# class PurchaseOrderSerializer(serializers.ModelSerializer):
#     """purchase serializers"""
#     class Meta:
#         """meta data"""
#         model = PurchaseOrder
#         fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['id', 'requisition', 'order_date', 'delivery_date', 'payment_terms',
                  'payment_due_date', 'shipping_method', 'delivery_address', 'approved_by']

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
