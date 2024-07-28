from rest_framework import serializers
from .models import SiteInspection


class SiteInspectionSerializer(serializers.ModelSerializer):
    """
    Serializer for the SiteInspection model.
    """

    class Meta:
        """inspection serializer meta data"""
        model = SiteInspection
        fields = '__all__'