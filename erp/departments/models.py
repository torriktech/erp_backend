# department and employee models
from django.db import models
# from django.conf import settings


class Department(models.Model):
    """department model"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    hod = models.ForeignKey(
        'auths.CustomUser',
        on_delete=models.CASCADE,
        related_name="department_head",
        null=True,
        blank=True)
    company = models.ForeignKey(
        'auths.CustomUser',
        on_delete=models.CASCADE,
        related_name="company",
        null=True,
        blank=True)
    
    
class Position(models.Model):
    """position model"""
    title = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
