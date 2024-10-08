from django.urls import path
from .views import (
    UserRegistrationView,
    CompanyRegistrationView,
    EmployeeRegistrationView,
    EmployeeProfileView,
    CompanyEmployeeListView,
    EmployeeListView,
    CompanyListView,
    #     CustomTokenObtainPairView,
    LoginView,
    CompanyProfileView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('register/company/',
         CompanyRegistrationView.as_view(), name='register_company'),
    path('register/employee/',
         EmployeeRegistrationView.as_view(), name='register_employee'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/employee/',
         EmployeeProfileView.as_view(), name='employee_profile'),
    path('company/employees/', CompanyEmployeeListView.as_view(),
         name='company-employee-list'),
    path('profile/company/',
         CompanyProfileView.as_view(), name='company_profile'),
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('companies/', CompanyListView.as_view(), name='company-list'),
]


