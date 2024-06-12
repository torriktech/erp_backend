from django.db import models
from django.conf import settings
from project.models import Project
from inventory.models import Inventory
from materials.models import Material


class Procurement(models.Model):
    confirmed_material = models.CharField(max_length=20)  # yes or no
    confirmed_payment = models.CharField(max_length=20)
    workers_payment_request = models.CharField(max_length=20)
    stores_request = models.CharField(max_length=20)
    inventory = models.CharField(max_length=20)
    supplier = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="assigned_tasks"
    )
    document = models.FileField(upload_to='attachments/')
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='projects',
        null=True, blank=True
    )
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name='procurements',
        null=True, blank=True
    )

    # purchase_order = models.OneToOneField(PurchaseOrder,
    # on_delete=models.CASCADE, null=True, blank=True)
    # documentation = models.OneToOneField(Documentation,
    # on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Procurement-{self.id}"


class Requisition(models.Model):
    """
    Model representing a requisition for procurement.
    """
    STATUS_CHOICES = [
        ('rejected', 'rejected'),
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    ]
    date = models.DateField()
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name='inventory_items')
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)
    remark = models.TextField(blank=True, null=True)
    procurement = models.ForeignKey(
        Procurement,
        on_delete=models.CASCADE,
        related_name='requisitions'
    )
    assigned_to = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="assigned_tasks"
    )
    approval_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    def __str__(self):
        return f"Requisition-{self.id} for Procurement-{self.procurement.id}"
