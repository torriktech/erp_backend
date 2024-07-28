# client model props
from django.db import models
from cloudinary.models import CloudinaryField

class Client(models.Model):
    """
    Model representing a client info.
    """
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    image = CloudinaryField('image', blank=True, null=True)
    site_address = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"client-{self.id}"
