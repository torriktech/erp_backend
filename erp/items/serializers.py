# items serializer
from rest_framework import serializers
from .models import Item
from category.serializers import CategorySerializer


class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the Item model.

    This serializer converts Item instances to JSON format and vice versa.
    """
    category = CategorySerializer(read_only=True)

    class Meta:
        """
        Meta class to specify the model and fields to
        be included in the serializer.
        """
        model = Item
        fields = "__all__"
