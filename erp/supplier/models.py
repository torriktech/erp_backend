# Supplier models
from django.db import models


class Supplier(models.Model):
    """supplier schemas"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


