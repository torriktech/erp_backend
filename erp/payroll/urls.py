# urls for payrolls
from django.urls import path
from .views import (
    AppraisalCreateView,
    AppraisalListView,
    AppraisalRetrieveView,
    AppraisalUpdateView,
    AppraisalDestroyView,
    PayrollCreateView,
    PayrollListView,
    PayrollRetrieveView,
    PayrollUpdateView,
    PayrollDestroyView,
    EmployeeAppraisalsView,
    EmployeePayrollsView
)

urlpatterns = [
    # Appraisal URLs
    path('appraisals/', AppraisalCreateView.as_view(), name='appraisal-create'),
    path('appraisals/', AppraisalListView.as_view(), name='appraisal-list'),
    path('appraisals/<int:pk>/',
         AppraisalRetrieveView.as_view(), name='appraisal-retrieve'),
    path('appraisals/<int:pk>/',
         AppraisalUpdateView.as_view(), name='appraisal-update'),
    path('appraisals/<int:pk>/',
         AppraisalDestroyView.as_view(), name='appraisal-destroy'),
    path('appraisals/employees/<int:employee_id>/',
         EmployeeAppraisalsView.as_view(), name='employee-appraisals'),
    
    # Payroll URLs
    path('create/', PayrollCreateView.as_view(), name='payroll-create'),
    path('list/', PayrollListView.as_view(), name='payroll-list'),
    path('retrieve/<int:pk>/',
         PayrollRetrieveView.as_view(), name='payroll-retrieve'),
    path('update/<int:pk>/',
         PayrollUpdateView.as_view(), name='payroll-update'),
    path('delete/<int:pk>/',
         PayrollDestroyView.as_view(), name='payroll-destroy'),
    path('employees/<int:employee_id>/',
         EmployeePayrollsView.as_view(), name='employee-payrolls'),
]
