# budget 
from rest_framework import serializers
from project.serializers import ProjectSerializer
from .models import Budget


class BudgetSerializer(serializers.ModelSerializer):
    """budget serializers"""    
    project_id = ProjectSerializer()
    
    class Meta:
        """budget meta data"""
        model = Budget
        fields = '__all__'
