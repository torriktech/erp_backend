"""purchase-order models"""
from django.db import models
from django.conf import settings
# from employee.models import Employee
from project.models import Project
from items.models import Item

STATUS_CHOICES = [
    ('pending', 'pending'),
    ('cancel', 'cancel'),
    ('approved', 'approved'),
    ('completed', 'completed'),
    ('on-progress', 'on-Progress'),
]


class Requisition(models.Model):
    """Requisition model schema

    Args:
        models (_type_): requisition model
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    project = models.ForeignKey(
        "project.Project",
        on_delete=models.CASCADE,
        related_name="requisitions"
    )
    item_id = models.ForeignKey(
        "items.Item",
        on_delete=models.CASCADE,
        related_name="requisitions",
        blank=True,
    )
    complain = models.CharField(max_length=255, blank=True, null=True),
    requested_by = models.ForeignKey(
        "auths.Employee",
        on_delete=models.CASCADE,
        related_name="emp_req_requisitions"
    )
    description = models.TextField()
    schedule_date = models.DateTimeField()
    approval_status = models.IntegerField()
    task = models.CharField(max_length=255)
    approve_by = models.ForeignKey(
        "auths.Employee",
        on_delete=models.CASCADE,
        related_name="emp_app_requisitions"
    )

    def __str__(self):
        return f'Requisition {self.id} for Project {self.project}'
    

class PurchaseOrder(models.Model):
    """Purchase Order model schema"""
    id = models.AutoField(primary_key=True)
    requisition = models.ForeignKey(
        Requisition,
        on_delete=models.CASCADE,
        related_name="purchase_orders"
    )
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    payment_terms = models.CharField(max_length=255)
    payment_due_date = models.DateTimeField()
    shipping_method = models.CharField(max_length=255)
    delivery_address = models.TextField()
    approved_by = models.ForeignKey(
        "auths.Employee",
        on_delete=models.CASCADE,
        related_name="created_by"
    )

    def __str__(self):
        return f'Purchase Order {self.id} for Requisition {self.requisition}'


class RequisitionItem(models.Model):
    """Requisition Item model schema"""
    id = models.AutoField(primary_key=True)
    requisition = models.ForeignKey(
        Requisition,
        on_delete=models.CASCADE,
        related_name="items"
    )
    item = models.ForeignKey(
        "items.Item",
        on_delete=models.CASCADE,
        related_name="requisition_items"
    )
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f'Item {self.item.name} for Requisition {self.requisition}'

# class Invoice(models.Model):
#     """
#     Model representing an invoice for a purchase order.

#     Fields:
#     - purchase_order: OneToOneField to PurchaseOrder model
#     - number: Invoice number
#     - date: Date of the invoice
#     - amount: Amount of the invoice
#     - payment_status: Payment status of the invoice
#     - payment_date: Date when payment was made for the invoice
#     """
#     purchase_order = models.OneToOneField(
#         PurchaseOrder, on_delete=models.CASCADE)
#     number = models.CharField(max_length=50)
#     date = models.DateField()
#     amount = models.DecimalField(max_digits=15, decimal_places=2)
#     payment_status = models.CharField(max_length=20,
#                                       choices=STATUS_CHOICES,
#                                       default='pending')
#     payment_date = models.DateField()

#     def __str__(self):
#         return self.number


# class Approval(models.Model):
#     """
#     Model representing an approval for a purchase order.

#     Fields:
#     - purchase_order: OneToOneField to PurchaseOrder model
#     - status: Status of the approval
#     - approver_name: Name of the approver
#     - approval_date: Date when the approval was granted
#     """

#     purchase_order = models.OneToOneField(
#         PurchaseOrder,
#         on_delete=models.CASCADE
#     )
#     status = models.CharField(max_length=20,
#                               choices=STATUS_CHOICES,
#                               default='pending')
#     approver_name = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="approved_by"
#     )
#     approval_date = models.DateField()

#     def __str__(self):
#         """_str_

#         Returns:
#             _type_: return the status
#         """
#         return self.status


# class Delivery(models.Model):
#     """
#     Model representing a delivery for a purchase order.

#     Fields:
#     - purchase_order: OneToOneField to PurchaseOrder model
#     - status: Status of the delivery
#     - received_quantity: Quantity received
#     - received_date: Date when the delivery was received
#     - receiving_personnel: Personnel who received the delivery
#     """

#     purchase_order = models.OneToOneField(
#         PurchaseOrder, on_delete=models.CASCADE)
#     status = models.CharField(max_length=20,
#                               choices=STATUS_CHOICES,
#                               default='pending')
#     received_quantity = models.DecimalField(max_digits=10, decimal_places=2)
#     received_date = models.DateField()
#     receiving_personnel = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="receiving_personnel"
#     )

#     def __str__(self):
#         return self.status


# class QualityControl(models.Model):
#     """
#     Model representing quality control for a purchase order.

#     Fields:
#     - purchase_order: OneToOneField to PurchaseOrder model
#     - status: Status of the quality control
#     - inspection_date: Date of the inspection
#     - quality_control_personnel: Personnel responsible for quality control
#     """
#     name = models.CharField(max_length=100)
#     status = models.CharField(max_length=20,
#                               choices=STATUS_CHOICES,
#                               default='pending')
#     purchase_order = models.OneToOneField(
#         PurchaseOrder,
#         on_delete=models.CASCADE
#     )
#     inspection_date = models.DateField()
#     quality_control_personnel = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="control_manager"
#     )

#     def __str__(self):
#         return self.status


# class Contract(models.Model):
#     """
#     Model representing a contract for a purchase order.

#     Fields:
#     - purchase_order: OneToOneField to PurchaseOrder model
#     - number: Contract number
#     - terms: Terms of the contract
#     - start_date: Start date of the contract
#     - end_date: End date of the contract
#     - renewal_date: Date for contract renewal
#     """

#     purchase_order = models.OneToOneField(
#         PurchaseOrder, on_delete=models.CASCADE)
#     number = models.CharField(max_length=50)
#     terms = models.TextField()
#     start_date = models.DateField()
#     end_date = models.DateField()
#     renewal_date = models.DateField()

#     def __str__(self):
#         return self.number


# class Documentation(models.Model):
#     """
#     Model representing documentation for a purchase order.

#     Fields:
#     - purchase_order: OneToOneField to PurchaseOrder model
#     - attachments: FileField for attachments related to the documentation
#     - notes: Additional notes for the documentation
#     """

#     purchase_order = models.OneToOneField(
#         PurchaseOrder,
#         on_delete=models.CASCADE
#     )
#     attachments = models.FileField(upload_to='attachments/')
#     notes = models.TextField()

#     def __str__(self):
#         return f"Documentation for PO-{self.purchase_order.id}"
