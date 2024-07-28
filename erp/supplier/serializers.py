# supplier serializer
from rest_framework import serializers
from .models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """
    Serializer for the Supplier model.
    """
    class Meta:
        """addition data for the serializer"""
        model = Supplier
        fields = '__all__'
        