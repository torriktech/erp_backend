from rest_framework import generics
from auths.models import Employee
from auths.serializers import EmployeeProfileSerializer
from .models import Department, Position
from .serializers import DepartmentSerializer, PositionSerializer


class EmployeeListView(generics.ListAPIView):
    """
    View to list all Employee instances.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeProfileSerializer


class EmployeeListByDepartmentView(generics.ListAPIView):
    """
    View to list all Employee base on department.
    """
    serializer_class = EmployeeProfileSerializer

    def get_queryset(self):
        department_id = self.kwargs['department_id']
        return Employee.objects.filter(department_id=department_id)
    


class EmployeeDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a specific Employee instance by its ID.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeProfileSerializer


class EmployeeUpdateView(generics.UpdateAPIView):
    """
    View to update a specific Employee instance by its ID.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeProfileSerializer


class EmployeeDestroyView(generics.DestroyAPIView):
    """
    View to delete a specific Employee instance by its ID.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeProfileSerializer


class DepartmentListView(generics.ListAPIView):
    """
    View to list all Department instances.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentCreateView(generics.CreateAPIView):
    """
    View to create a new Department instance.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a specific Department instance by its ID.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentUpdateView(generics.UpdateAPIView):
    """
    View to update a specific Department instance by its ID.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDestroyView(generics.DestroyAPIView):
    """
    View to delete a specific Department instance by its ID.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionListCreateView(generics.ListCreateAPIView):
    """
    View to create or list a positions
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """View to update, retrive or destroy specific position using ID."""
    queryset = Position.objects.all()
    serializer_class = PositionSerializer