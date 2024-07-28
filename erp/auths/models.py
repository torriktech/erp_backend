# auths models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField
from payroll.models import Payroll
from departments.models import Department, Position


class CustomUser(AbstractUser):
    """custom user definition"""
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(
        Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(
        Permission, related_name='customuser_set_permissions')
    # role fields
    is_employee = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)


class CompanyProfile(models.Model):
    """company profile"""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=255)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=20)
    logo = CloudinaryField('image', blank=True, null=True)
    

    def __str__(self):
        return self.company_name
    

class Employee(models.Model):
    """Employee model"""
    id = models.AutoField(primary_key=True)
    department_id = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="employee")
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=True, null=True)
    email = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    state = models.CharField(max_length=50, null=False, blank=False)
    hired_date = models.DateTimeField()
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        "CompanyProfile",
        on_delete=models.CASCADE,
        related_name='employees'
    )
    payroll_id = models.ForeignKey(
        Payroll,
        on_delete=models.CASCADE,
        related_name="employee_payroll")
    
