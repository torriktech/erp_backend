"""bill of quanity model"""
from django.db import models
from cloudinary.models import CloudinaryField

class Key(models.Model):
    """
    Model representing key details for Bill of Quantity.
    """
    type = models.CharField(max_length=255)
    description = models.TextField()
    unitMeasurement = models.CharField(max_length=50)
    quantity = models.FloatField()
    rate = models.FloatField()
    total = models.FloatField()

    def __str__(self):
        return f"{self.type} - {self.description}"


class BillOfQuantity(models.Model):
    """
    Model representing Bill of Quantity details.
    """
    description = models.CharField(max_length=255)
    equipment_cost = models.FloatField(null=True, blank=True)
    estimated_cost = models.FloatField(null=True, blank=True)
    sub_contractor_cost = models.FloatField(null=True, blank=True)
    material_cost = models.FloatField(null=True, blank=True)
    labour_cost = models.FloatField(null=True, blank=True)
    mark_up_cost = models.FloatField(null=True, blank=True)
    file = CloudinaryField('image', blank=True, null=True)
    key = models.ForeignKey(
        Key,
        related_name="boq_keys",
        on_delete=models.CASCADE)
    project_id = models.ForeignKey(
        'project.Project',
        related_name='boq_project',
        on_delete=models.CASCADE
    )

