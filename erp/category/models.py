"""category"""
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """
    Model representing a category for items or products.
    """
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta class for Category model to define additional properties.
        """
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

