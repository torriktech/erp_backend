"""purchase-order models"""
from django.db import models
from procurement.models import Procurement


class PurchaseOrder(models.Model):
    """
    Model representing a purchase order.

    Fields:
    - procurement: ForeignKey to Procurement model
    - order_date: Date when the order was placed
    - expected_delivery_date: Date expected for delivery
    - payment_terms: Payment terms for the order
    - payment_due_date: Date by which payment is due
    - shipping_method: Method of shipping for the order
    - delivery_address: Address where the order is to be delivered
    """

    procurement = models.ForeignKey(Procurement, on_delete=models.CASCADE)
    order_date = models.DateField()
    expected_delivery_date = models.DateField()
    payment_terms = models.CharField(max_length=50)
    payment_due_date = models.DateField()
    shipping_method = models.CharField(max_length=100)
    delivery_address = models.TextField()

    def __str__(self):
        return f"PO-{self.id}"


class Approval(models.Model):
    """
    Model representing an approval for a purchase order.

    Fields:
    - purchase_order: OneToOneField to PurchaseOrder model
    - status: Status of the approval
    - approver_name: Name of the approver
    - approval_date: Date when the approval was granted
    """

    purchase_order = models.OneToOneField(
        PurchaseOrder,
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=20)
    approver_name = models.CharField(max_length=100)
    approval_date = models.DateField()

    def __str__(self):
        return self.status


class Delivery(models.Model):
    """
    Model representing a delivery for a purchase order.

    Fields:
    - purchase_order: OneToOneField to PurchaseOrder model
    - status: Status of the delivery
    - received_quantity: Quantity received
    - received_date: Date when the delivery was received
    - receiving_personnel: Personnel who received the delivery
    """

    purchase_order = models.OneToOneField(PurchaseOrder, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    received_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    received_date = models.DateField()
    receiving_personnel = models.CharField(max_length=100)

    def __str__(self):
        return self.status

class Invoice(models.Model):
    """
    Model representing an invoice for a purchase order.

    Fields:
    - purchase_order: OneToOneField to PurchaseOrder model
    - number: Invoice number
    - date: Date of the invoice
    - amount: Amount of the invoice
    - payment_status: Payment status of the invoice
    - payment_date: Date when payment was made for the invoice
    """

    purchase_order = models.OneToOneField(PurchaseOrder, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    payment_status = models.CharField(max_length=20)
    payment_date = models.DateField()

    def __str__(self):
        return self.number

class QualityControl(models.Model):
    """
    Model representing quality control for a purchase order.

    Fields:
    - purchase_order: OneToOneField to PurchaseOrder model
    - status: Status of the quality control
    - inspection_date: Date of the inspection
    - quality_control_personnel: Personnel responsible for quality control
    """

    purchase_order = models.OneToOneField(
        PurchaseOrder,
        on_delete=models.CASCADE
    )
    status = models.CharField(max_length=20)
    inspection_date = models.DateField()
    quality_control_personnel = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class Contract(models.Model):
    """
    Model representing a contract for a purchase order.

    Fields:
    - purchase_order: OneToOneField to PurchaseOrder model
    - number: Contract number
    - terms: Terms of the contract
    - start_date: Start date of the contract
    - end_date: End date of the contract
    - renewal_date: Date for contract renewal
    """

    purchase_order = models.OneToOneField(PurchaseOrder, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    terms = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    renewal_date = models.DateField()

    def __str__(self):
        return self.number


class Documentation(models.Model):
    """
    Model representing documentation for a purchase order.

    Fields:
    - purchase_order: OneToOneField to PurchaseOrder model
    - attachments: FileField for attachments related to the documentation
    - notes: Additional notes for the documentation
    """

    purchase_order = models.OneToOneField(
        PurchaseOrder,
        on_delete=models.CASCADE
    )
    attachments = models.FileField(upload_to='attachments/')
    notes = models.TextField()

    def __str__(self):
        return f"Documentation for PO-{self.purchase_order.id}"