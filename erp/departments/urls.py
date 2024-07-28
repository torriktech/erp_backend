# employe and department endpoints
from django.urls import path
from .views import (
    DepartmentListView,
    DepartmentCreateView,
    DepartmentDetailView,
    DepartmentUpdateView,
    DepartmentDestroyView,
    EmployeeListView,
    EmployeeDetailView,
    EmployeeUpdateView,
    EmployeeDestroyView,
    EmployeeListByDepartmentView,
    PositionListCreateView,
    PositionRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Department endpoints
    path('',
         DepartmentListView.as_view(), name='department-list'),
    path('create/',
         DepartmentCreateView.as_view(), name='department-create'),
    path('<int:pk>/',
         DepartmentDetailView.as_view(), name='department-detail'),
    path('<int:pk>/update/',
         DepartmentUpdateView.as_view(), name='department-update'),
    path('<int:pk>/delete/',
         DepartmentDestroyView.as_view(), name='department-delete'),

    # Employee endpoints
    path('employees/',
         EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/',
         EmployeeDetailView.as_view(), name='employee-detail'),
    path('employees/<int:pk>/update/',
         EmployeeUpdateView.as_view(), name='employee-update'),
    path('employees/<int:pk>/delete/',
         EmployeeDestroyView.as_view(), name='employee-delete'),
    path('emp-dept/<int:department_id>/',
         EmployeeListByDepartmentView.as_view(),
         name='employees-by-department'),
     # Positions
    path('positions/', PositionListCreateView.as_view(),
         name='position-list-create'),
    path('positions/<int:pk>/', PositionRetrieveUpdateDestroyView.as_view(),
         name='position-retrieve-update-destroy'),
]

