from django.contrib.auth import authenticate, get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.models import Token
from .serializers import (
    CustomUserSerializer,
    CompanyProfileSerializer,
    EmployeeProfileSerializer
)
from .models import CompanyProfile, Employee
User = get_user_model()


class UserRegistrationView(generics.CreateAPIView):
    """user registration view"""
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


class CompanyRegistrationView(generics.CreateAPIView):
    """company registration view"""
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    permission_classes = [permissions.AllowAny]


class EmployeeRegistrationView(generics.CreateAPIView):
    """employee registration view"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_context(self):
        """Passes request to serializer context"""
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class EmployeeProfileView(generics.RetrieveUpdateAPIView):
    """employee profile"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.employee
    

class CompanyProfileView(generics.RetrieveUpdateAPIView):
    """company profile"""
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.company_profile


class CustomTokenObtainPairView(TokenObtainPairView):
    """login user"""
    serializer_class = CustomUserSerializer


class LoginView(TokenObtainPairView):
    """
    Login view using SimpleJWT.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            'refresh': response.data['refresh'],
            'access': response.data['access'],
        }, status=status.HTTP_200_OK)
    
# class LoginView(APIView):
#     """login view"""
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, *args, **kwargs):
#         """post for login"""
#         username = request.data.get('username')
#         password = request.data.get('password')
#         print(f"Attempting to authenticate user: {username}")  # Debug print
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({
#                     'token': token.key,
#                 }, status=status.HTTP_200_OK)
#             else:
#                 return Response({"detail": "User account is inactive."}, status=status.HTTP_401_UNAUTHORIZED)
#         return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


