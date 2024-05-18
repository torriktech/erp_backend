from django.urls import path
from .views import (
    ProjectListCreateAPIView,
    ProjectDetailAPIView,
    ProjectOperationCreateAPIView,
    ProjectOperationDetailAPIView,
    TaskListCreateAPIView,
    TaskDetailAPIView,
    MilestoneListCreateAPIView,
    MilestoneDetailAPIView
)

urlpatterns = [
    path('',
         ProjectListCreateAPIView.as_view(),
         name='project-list-create'),
    path('<int:pk>/',
         ProjectDetailAPIView.as_view(),
         name='project-detail'),
    path('<int:project_id>/operations/',
         ProjectOperationCreateAPIView.as_view(),
         name='project-operation-create'),
    path('operations/<int:pk>/',
         ProjectOperationDetailAPIView.as_view(),
         name='project-operation-detail'),
    path('tasks/',
         TaskListCreateAPIView.as_view(),
         name='task-list-create'),
    path('tasks/<int:pk>/',
         TaskDetailAPIView.as_view(),
         name='task-detail'),
    path('milestones/',
         MilestoneListCreateAPIView.as_view(),
         name='milestone-list-create'),
    path('milestones/<int:pk>/',
         MilestoneDetailAPIView.as_view(),
         name='milestone-detail'),
]
