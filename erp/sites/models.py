"""site model definition"""
from django.conf import settings
from django.db import models
from project.models import ProjectOperation


class SiteInspection(models.Model):
    """
    Model representing a site inspection.
    """
    date = models.DateField()
    sitename = models.CharField(max_length=255)
    stage = models.CharField(max_length=255)
    remark = models.TextField()
    inspection_officer = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="assigned_tasks"
    )
    image = models.ImageField(
        upload_to='site_inspections/',
        blank=True,
        null=True
    )
    project_operation = models.ForeignKey(
        ProjectOperation,
        on_delete=models.CASCADE,
        related_name="inspections"
    )
    
    def __str__(self):
        return f'Inspection at {self.sitename} on {self.date}'