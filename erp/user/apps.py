from django.apps import AppConfig

class UserConfig(AppConfig):
    """
    Custom configuration class for the 'user' Django app.
    This class is used to define specific behaviors and configurations
    when the app is initialized.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    """
    Specifies the default auto-incrementing field type for primary keys.
    'BigAutoField' is a 64-bit integer, commonly used for large databases or
    when a high number of records is expected.
    """

    name = 'user'
    """
    The name of the Django app. This name should match the folder name where
    the app resides and is used by Django to identify this app within the project.
    """

    def ready(self):
        """
        This method is called when the app is initialized. It's often used to
        perform additional setup, like importing signals, connecting signal handlers,
        or initializing other resources needed by the app.
        """
        import user.signals
        """
        Importing the 'user.signals' module ensures
        that Django recognizes and registers
        any signals defined there. This is commonly used
        for setting up signal handlers,
        which perform specific actions when certain events occur,
        like creating a user profile
        upon user creation.
        """
