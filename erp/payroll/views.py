from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from auths.models import Employee
from .models import Appraisal, Payroll
from .serializers import AppraisalSerializer, PayrollSerializer


# Views for Appraisal

class AppraisalCreateView(generics.CreateAPIView):
    """
    View to create a new appraisal instance.
    """
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer


class AppraisalListView(generics.ListAPIView):
    """
    View to list all appraisal instances.
    """
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer


class AppraisalRetrieveView(generics.RetrieveAPIView):
    """
    View to retrieve a specific appraisal instance by its ID.
    """
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer


class AppraisalUpdateView(generics.UpdateAPIView):
    """
    View to update a specific appraisal instance by its ID.
    """
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer


class AppraisalDestroyView(generics.DestroyAPIView):
    """
    View to delete a specific appraisal instance by its ID.
    """
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer


class EmployeeAppraisalsView(APIView):
    """get appraisal base on employee"""

    def get(self, request, employee_id):
        """get record"""
        employee = get_object_or_404(Employee, id=employee_id)
        appraisals = Appraisal.objects.filter(employee=employee)
        serializer = AppraisalSerializer(appraisals, many=True)
        return Response(serializer.data)


# Views for Payroll
class EmployeePayrollsView(APIView):
    """get payroll base on employee"""

    def get(self, request, employee_id):
        """get record"""
        employee = get_object_or_404(Employee, id=employee_id)
        payrolls = Payroll.objects.filter(employee=employee)
        serializer = PayrollSerializer(payrolls, many=True)
        return Response(serializer.data)
    

class PayrollCreateView(generics.CreateAPIView):
    """
    View to create a new payroll instance.
    """
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer


class PayrollListView(generics.ListAPIView):
    """
    View to list all payroll instances.
    """
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer


class PayrollRetrieveView(generics.RetrieveAPIView):
    """
    View to retrieve a specific payroll instance by its ID.
    """
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer


class PayrollUpdateView(generics.UpdateAPIView):
    """
    View to update a specific payroll instance by its ID.
    """
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer


class PayrollDestroyView(generics.DestroyAPIView):
    """
    View to delete a specific payroll instance by its ID.
    """
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
