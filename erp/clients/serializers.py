# serializser 
from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Client model.
    Converts model instances to JSON and vice versa.
    """
    class Meta:
        """additional data"""
        model = Client
        fields = '__all__'
