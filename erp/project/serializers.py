"""serializer for project"""
from rest_framework import serializers
from .models import (
    Project,
    ProjectOperation,
    Task,
    Milestone
)


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.

    Fields:
    --------
    All fields from the Project model are included.

    Usage:
    --------
    Used to serialize/deserialize Project instances to/from JSON format.
    """
    class Meta:
        '''project meta data'''
        model = Project
        fields = '__all__'


class ProjectOperationSerializer(serializers.ModelSerializer):
    """
    Serializer for the ProjectOperation model.

    Fields:
    --------
    All fields from the ProjectOperation model are included.

    Usage:
    --------
    Used to serialize/deserialize ProjectOperation instances to/from JSON format.
    """
    class Meta:
        '''project operation meta data'''
        model = ProjectOperation
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.

    Fields:
    --------
    All fields from the Task model are included.

    Usage:
    --------
    Used to serialize/deserialize Task instances to/from JSON format.
    """
    class Meta:
        '''task meta data'''
        model = Task
        fields = '__all__'


class MilestoneSerializer(serializers.ModelSerializer):
    """
    Serializer for the Milestone model.

    Fields:
    --------
    All fields from the Milestone model are included.

    Usage:
    --------
    Used to serialize/deserialize Milestone instances to/from JSON format.
    """
    class Meta:
        '''milestone meta data'''
        model = Milestone
        fields = '__all__'
