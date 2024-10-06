from django.db import models
from django.utils import timezone


class Cashbook(models.Model):
    """cashbook model"""
    TRANSACTION_TYPES = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]
    project = models.ForeignKey(
        "project.Project",
        on_delete=models.CASCADE,
        related_name="cashbook",
        null=True,
        blank=True,
    )
    date = models.DateField(default=timezone.now)
    description = models.CharField(max_length=255)
    voucher_number = models.CharField(max_length=50, unique=True)
    transaction_type = models.CharField(
        max_length=7,
        choices=TRANSACTION_TYPES
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.description} - {self.transaction_type}"
