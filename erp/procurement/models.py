from django.db import models
from supplier.models import Supplier
from project.models import Project


class Procurement(models.Model):
    confirmed_material = models.CharField(max_length=20)  # yes or no
    confirmed_payment = models.CharField(max_length=20)
    workers_payment_request = models.CharField(max_length=20)
    stores_request = models.CharField(max_length=20)
    inventory = models.CharField(max_length=20)
    supplier = models.ForeignKey(Supplier,
                                 on_delete=models.CASCADE,
                                 related_name='procurements'
                                )
    document = models.FileField(upload_to='attachments/')
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='projects',
        null=True, blank=True
    )

    # purchase_order = models.OneToOneField(PurchaseOrder,
    # on_delete=models.CASCADE, null=True, blank=True)
    # documentation = models.OneToOneField(Documentation,
    # on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Procurement-{self.id}"


