# budget 
from rest_framework import serializers
from project.serializers import ProjectSerializer
from .models import Budget
from project.models import Project

# class BudgetSerializer(serializers.ModelSerializer):
#     """budget serializers"""    
#     project_id = ProjectSerializer()
    
#     class Meta:
#         """budget meta data"""
#         model = Budget
#         fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField to allow passing just the ID of the project
    project_id = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), source='project')

    class Meta:
        model = Budget
        fields = ['id', 'project_id', 'budget_position', 'start_date', 'end_date', 'planned_amount', 'practical_amount', 'paid_amount', 'paid_date']

