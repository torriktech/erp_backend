"""bill of quanity model"""
from django.db import models


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
    equipment_cost = models.FloatField()
    estimated_cost = models.FloatField()
    sub_contractor_cost = models.FloatField(null=True, blank=True)
    material_cost = models.FloatField()
    labour_cost = models.FloatField()
    mark_up_cost = models.FloatField()
    key = models.ForeignKey(Key, on_delete=models.CASCADE)
