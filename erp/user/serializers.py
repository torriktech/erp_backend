'''user model serializer'''
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from user.models import UserModel
from django.contrib.auth.hashers import make_password



class UserSerializer(serializers.ModelSerializer):
    '''user model serializer class'''
    class Meta:
        '''a meta class for the user serializer'''
        fields = '__all__'
        model = UserModel
        extra_kwargs = {'password': {'write_only': True}}


class RegisterUserSerializer(serializers.Serializer):
    """
    Serializer for user registration.
    This serializer validates the required fields and ensures
    the username and email are unique.
    """
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"})

    def validate_username(self, value):
        """
        Validate that the username is unique.
        """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already taken.")
        return value

    def validate_email(self, value):
        """
        Validate that the email is unique.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value

    def create(self, validated_data):
        """
        Create a new user with the provided data, hashing the password.
        """
        validated_data['password'] = make_password(validated_data['password'])  # Hash the password
        user = User.objects.create(**validated_data)  # Create user with hashed password
        return user



class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login. It validates the required fields and provides
    a method to authenticate the user.
    """
    username = serializers.CharField(
        max_length=150,
        required=True,
        error_messages={
            "blank": _("Username cannot be blank."),
            "required": _("Username is required."),
        },
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"},
        error_messages={
            "blank": _("Password cannot be blank."),
            "required": _("Password is required."),
        },
    )

    def validate(self, data):
        """
        Custom validation method to authenticate
        the user with provided credentials.
        """
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            raise serializers.ValidationError(_("Both username and password\
                                                are required."))

        # Authenticate the user with the given credentials
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(_("Invalid username or password."))

        if not user.is_active:
            raise serializers.ValidationError(_("This account is inactive."))

        # Store the user in the context to be used by the view
        data["user"] = user
        return data