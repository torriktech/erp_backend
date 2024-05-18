'''user model'''
from django.db import models
from django.contrib.auth.models import User


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
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''str method for the current users'''
        return f'user -> {self.email}'
