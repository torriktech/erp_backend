# department and employee models
from django.db import models
from django.conf import settings
# Create your models here.


class Department(models.Model):
    """department model"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    hod = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="department_head")


class Position(models.Model):
    """position model"""
    title = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


