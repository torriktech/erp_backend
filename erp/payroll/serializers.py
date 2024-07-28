"""serializer module for Appraisal and Payroll"""
from rest_framework import serializers
from .models import Appraisal, Payroll


class AppraisalSerializer(serializers.ModelSerializer):
    """Appraisal serializer"""
    class Meta:
        """appraisal meta data"""
        model = Appraisal
        fields = '__all__'


class PayrollSerializer(serializers.ModelSerializer):
    """Payroll serializer"""
    class Meta:
        """Payroll meta data"""
        model = Payroll
        fields = '__all__'
