# Create your models here.
from django.db import models
from project.models import Project


class Budget(models.Model):
    """Budget model schema
    Args:
        models (_type_): budget model
    """
    id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="budgets"
    )
    budget_position = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    planned_amount = models.FloatField()
    practical_amount = models.FloatField()
    paid_amount = models.FloatField()
    paid_date = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Budget for {self.project_id.name}'
