from django.urls import path
from .views import (
    UserRegistrationView, 
    CompanyRegistrationView, 
    EmployeeRegistrationView,
    EmployeeProfileView, 
    CompanyProfileView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('register/company/',
         CompanyRegistrationView.as_view(), name='register_company'),
    path('register/employee/',
         EmployeeRegistrationView.as_view(), name='register_employee'),
#     path('login/', LoginView.as_view(), name='login'),
    path('profile/employee/',
         EmployeeProfileView.as_view(), name='employee_profile'),
    path('profile/company/',
         CompanyProfileView.as_view(), name='company_profile'),
]
