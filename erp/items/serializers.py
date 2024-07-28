# items serializer
from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the Item model.

    This serializer converts Item instances to JSON format and vice versa.
    """

    class Meta:
        """
        Meta class to specify the model and fields to
        be included in the serializer.
        """
        model = Item
        fields = '__all__'
