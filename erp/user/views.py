'''user views'''
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.serializers import Serializer, CharField, ValidationError

# custom functions anc lasses
from .serializers import UserSerializer, LoginSerializer
from .models import UserModel


class RegisterUser(APIView):
    """
    Endpoint for user account creation (registration).
    This creates a new base user account in the Django `User` model.
    """

    def post(self, request):
        """
        Create a new user account with basic information.
        """
        # Validate and create the user account with the required fields
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return Response(
                {"error": "Username, password, and email are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username is already taken."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "Email is already registered."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create the new user
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password),
        )

        # Create a related UserModel record for additional information
        User.objects.create(user=user)

        return Response(
            {"message": "User registered successfully."},
            status=status.HTTP_201_CREATED,
        )


class LoginUser(ObtainAuthToken):
    """
    API view to log in a user.
    Validates user credentials and returns an authentication token upon success.
    """

    def post(self, request, *args, **kwargs):
        """
        Authenticates the user and returns an authentication token.
        If credentials are invalid, returns an appropriate error response.
        """
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        user = serializer.validated_data["user"]

        if user is None:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Get or create the token for the authenticated user
        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "user_id": user.id,
                "username": user.username,
            },
            status=status.HTTP_200_OK,
        )


class UpdateUserProfile(APIView):
    """
    Endpoint for updating user profile information.
    Allows users to update additional details after account creation.
    """
    permission_classes = [IsAuthenticated]

    def put(self, request):
        """
        Update the user's profile with additional information.
        """
        user = request.user
        profile = UserModel.objects.get(user=user)

        serializer = UserSerializer(profile, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()  # Save the updated profile information
            return Response({"message": "Profile updated successfully."},
                            status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUser(APIView):
    """
    Endpoint to delete a user account.
    Requires authentication, ensuring only the authenticated
      user can delete their own account.
    """
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        """
        Deletes the authenticated user's account from the database.
        """
        user = request.user

        try:
            user.delete()
            return Response(
                {"message": "User deleted successfully."},
                status=status.HTTP_200_OK,
            )
        except IntegrityError:
            return Response(
                {"error": "Error deleting user."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class LogoutUser(APIView):
    """
    API view to log out a user.
    Allows authenticated users to log out by deleting their authentication token.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Logs out the current user by deleting the authentication token.
        """
        # Delete the authentication token to log out
        request.user.auth_token.delete()
        # Perform Django's logout operation
        logout(request)
        return Response({"message": "User logged out successfully"},
                        status=status.HTTP_200_OK)
