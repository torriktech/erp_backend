from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'  # Alternatively, specify fields explicitly: ['id', 'name', 'contact_email', ...]
