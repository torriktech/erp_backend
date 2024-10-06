from rest_framework import serializers
from .models import Cashbook


class CashbookSerializer(serializers.ModelSerializer):
    """serializer for cashbook"""
    class Meta:
        model = Cashbook
        fields = ['id', 'date', 'description', 'voucher_number', 'project', 'transaction_type', 'amount', 'balance']
