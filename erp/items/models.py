# items model definition
from django.db import models
from category.models import Category
from cloudinary.models import CloudinaryField


class Item(models.Model):
    """Item model schema

    Args:
        models (_type_): item model
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = CloudinaryField('image', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    unit_price = models.FloatField()
    quantity = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="items_category"
    )

    def __str__(self):
        '''string'''
        return self.name