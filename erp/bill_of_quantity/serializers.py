# serializers
from rest_framework import serializers
from .models import BillOfQuantity, Key


class KeySerializer(serializers.ModelSerializer):
    """key serializer"""
    class Meta:
        """key information"""
        model = Key
        fields = '__all__'


class BillOfQuantitySerializer(serializers.ModelSerializer):
    """bill of quantity serializer"""
    key = KeySerializer()
    project_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        """BOQ information"""
        model = BillOfQuantity
        fields = '__all__'
