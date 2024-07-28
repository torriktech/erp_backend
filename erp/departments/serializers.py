# employee serializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Department, Position
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """user infor serializer"""
    class Meta:
        """additional data"""
        model = User
        fields = ['id', 'username', 'email']


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Department model.
    This serializer converts the Department model
    instance into various formats such as JSON.
    It also validates data before saving it to the Department model.
    """
    class Meta:
        """meta data"""
        model = Department
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    """position serializer"""
    class Meta:
        """meta data"""
        model = Position
        fields = "__all__"