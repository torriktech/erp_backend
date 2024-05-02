
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserModel

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler that creates a user profile when a new user is created.
    """
    if created:
        # Create a new UserModel instance associated with the User
        UserModel.objects.create(user=instance)
