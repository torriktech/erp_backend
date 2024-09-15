from rest_framework import serializers
from .models import Budget
from project.models import Project


class BudgetSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField for 'project' to handle integer input correctly
    project_id = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Budget
        fields = ['id', 'project_id', 'budget_position', 'start_date', 'end_date', 'planned_amount', 'practical_amount', 'paid_amount', 'paid_date']

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'project_id' in validated_data:
            instance.project = validated_data.pop('project_id')
        return super().update(instance, validated_data)
