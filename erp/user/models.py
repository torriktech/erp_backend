'''user model'''
from django.db import models
from django.contrib.auth.models import User
from project.models import Project


class UserModel(models.Model):
    """
    This model extends the default Django user with additional information
    like mobile number, first name, last name, email, and creation date.
    """

    # Create a one-to-one relationship with Django's default User model
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    mobile_num = models.CharField(max_length=11)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    roles = models.CharField(max_length=150, blank=True)
    job_role = models.CharField(max_length=20)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    address = models.TextField()
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    projects = models.ManyToManyField(
        Project,
        related_name='users',
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''str method for the current users'''
        return f'user -> {self.first_name} {self.last_name}'
