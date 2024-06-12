from django.db import models


class Material(models.Model):
    """
    Model representing a material.
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name