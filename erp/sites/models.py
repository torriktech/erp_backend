"""site model definition"""
# from django.conf import settings
from django.db import models
from auths.models import CustomUser
from project.models import Project
from cloudinary.models import CloudinaryField


class SiteInspection(models.Model):
    """
    Model representing a site inspection.
    """
    date = models.DateField()
    sitename = models.CharField(max_length=255)
    stage = models.CharField(max_length=255)
    remark = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    inspection_officer = models.ManyToManyField(
        CustomUser,
        related_name="site_inspections"
    )
    image = CloudinaryField('image', blank=True, null=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="inspections"
    )
    
    def __str__(self):
        return f'Inspection at {self.sitename} on {self.date}'