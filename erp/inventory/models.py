from django.db import models
from materials.models import Material
    

class Inventory(models.Model):
    """
    Model representing an inventory item.
    """
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name='inventory_items')
    quantity = models.FloatField()
    amount_purchased = models.FloatField() # bought
    last_updated = models.DateField(auto_now=True)
    # how many material left in store
    instore = models.IntegerField()

    def __str__(self):
        return self.material.name
    