# serializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from departments.serializers import DepartmentSerializer
from .models import CustomUser, CompanyProfile, Employee


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for CustomUser model.

    Serializes fields and handles password hashing.
    """
    class Meta:
        """meta data"""
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True},
            'groups': {'required': False},
            'user_permissions': {'required': False},
        }
        
    def create(self, validated_data):
        """
        Create a new CustomUser with hashed password.

        Args:
            validated_data (dict): Validated data for user creation.

        Returns:
            CustomUser: The created user instance.
        """
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username'],
            is_employee=validated_data.get('is_employee', False),
            is_company=validated_data.get('is_company', False)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CompanyProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for CompanyProfile model.

    Handles nested creation of a company user and its profile.
    """
    user = CustomUserSerializer()

    class Meta:
        """meta data"""
        model = CompanyProfile
        fields = "__all__"

    def create(self, validated_data):
        """
        Create a new CompanyProfile with a nested user.

        Args:
            validated_data (dict): Validated data for company profile creation.

        Returns:
            CompanyProfile: The created company profile instance.
        """
        user_data = validated_data.pop('user')
        user = CustomUserSerializer.create(
            CustomUserSerializer(), validated_data=user_data)
        company_profile = CompanyProfile.objects.create(
            user=user, **validated_data)
        return company_profile


class EmployeeProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Employee model.

    Handles nested creation of an employee user and its profile.
    """
    user = CustomUserSerializer()
    department = DepartmentSerializer(read_only=True)

    class Meta:
        """meta data"""
        model = Employee
        fields = "__all__"

    # def create(self, validated_data):
        
    #     user_data = validated_data.pop('user')
    #     user = CustomUserSerializer.create(
    #         CustomUserSerializer(), validated_data=user_data)
    #     employee_profile = Employee.objects.create(
    #         user=user, **validated_data)
    #     return employee_profile

    def create(self, validated_data):
        """
        Create a new Employee with a nested user.

        Args:
            validated_data (dict): Validated data for employee creation.

        Returns:
            Employee: The created employee instance.
        """
        user_data = validated_data.pop('user')
        request = self.context.get('request')
        if not request.user.is_company:
            raise ValidationError("Only users with a company profile can create employees.")
        
        # Ensure the company profile exists for the user
        try:
            company_profile = request.user.company_profile
        except CompanyProfile.DoesNotExist:
            raise ValidationError("User does not have an associated company profile.")

        user = CustomUserSerializer.create(
            CustomUserSerializer(),
            validated_data=user_data
        )
        employee_profile = Employee.objects.create(
            user=user,
            company=company_profile,
            **validated_data
        )
        return employee_profile


