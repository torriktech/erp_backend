"""serializer for project"""
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Project, WorkSchedule, Details, Task, ProjectIssues
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users model."""
    class Meta:
        """additional data class"""
        model = User
        fields = ['id', 'username', 'email']


class WorkScheduleSerializer(serializers.ModelSerializer):
    """Serializer for the WorkSchedule model."""
    class Meta:
        """additional data class"""
        model = WorkSchedule
        fields = '__all__'


class DetailsSerializer(serializers.ModelSerializer):
    """Serializer for the Details model."""
    class Meta:
        """additional data class"""
        model = Details
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Task model."""
    class Meta:
        """additional data class"""
        model = Task
        fields = '__all__'


class ProjectIssuesSerializer(serializers.ModelSerializer):
    """Serializer for the ProjectIssues model."""
    class Meta:
        """additional data class"""
        model = ProjectIssues
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for the project model."""
    work_schedules = WorkScheduleSerializer(many=True, read_only=True)
    details = DetailsSerializer(many=True, read_only=True)
    project = TaskSerializer(many=True, read_only=True)
    timesheets = ProjectIssuesSerializer(many=True, read_only=True)
    # manager = serializers.StringRelatedField()

    class Meta:
        """additional data class"""
        model = Project
        fields = '__all__'
        

# class ProjectOperationSerializer(serializers.ModelSerializer):
#     """
#     Serializer for the ProjectOperation model.

#     Fields:
#     --------
#     All fields from the ProjectOperation model are included.

#     Usage:
#     --------
#     Used to serialize/deserialize ProjectOperation instances to/from JSON format.
#     """
#     class Meta:
#         '''project operation meta data'''
#         model = ProjectOperation
#         fields = '__all__'



# class MilestoneSerializer(serializers.ModelSerializer):
#     """
#     Serializer for the Milestone model.

#     Fields:
#     --------
#     All fields from the Milestone model are included.

#     Usage:
#     --------
#     Used to serialize/deserialize Milestone instances to/from JSON format.
#     """
#     class Meta:
#         '''milestone meta data'''
#         model = Milestone
#         fields = '__all__'
