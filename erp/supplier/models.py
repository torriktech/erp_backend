from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    address = models.TextField()
    payment_terms = models.CharField(max_length=50)
    lead_time = models.DurationField()

    def __str__(self):
        return self.name