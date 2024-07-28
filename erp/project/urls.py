from django.urls import path
from .views import (
    ProjectListView, ProjectCreateView, ProjectDetailView,
    ProjectUpdateView, ProjectDeleteView,
    WorkScheduleListView, WorkScheduleCreateView, WorkScheduleDetailView, 
    WorkScheduleUpdateView, WorkScheduleDeleteView,
    DetailsListView, DetailsCreateView, DetailsDetailView, DetailsUpdateView, DetailsDeleteView,
    TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView,
    ProjectIssuesListView, ProjectIssuesCreateView, ProjectIssuesDetailView, ProjectIssuesUpdateView, ProjectIssuesDeleteView
)

urlpatterns = [
    # Project URLs
    path('projects/',
         ProjectListView.as_view(), name='project-list'),
    path('projects/create/',
         ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/',
         ProjectDetailView.as_view(), name='project-detail'),
    path('projects/<int:pk>/update/',
         ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/',
         ProjectDeleteView.as_view(), name='project-delete'),

    # WorkSchedule URLs
    path('work-schedules/',
         WorkScheduleListView.as_view(), name='work-schedule-list'),
    path('work-schedules/create/',
         WorkScheduleCreateView.as_view(), name='work-schedule-create'),
    path('work-schedules/<int:pk>/',
         WorkScheduleDetailView.as_view(), name='work-schedule-detail'),
    path('work-schedules/<int:pk>/update/',
         WorkScheduleUpdateView.as_view(), name='work-schedule-update'),
    path('work-schedules/<int:pk>/delete/', WorkScheduleDeleteView.as_view(), name='work-schedule-delete'),

    # Details URLs
    path('details/', DetailsListView.as_view(), name='details-list'),
    path('details/create/', 
         DetailsCreateView.as_view(), name='details-create'),
    path('details/<int:pk>/',
         DetailsDetailView.as_view(), name='details-detail'),
    path('details/<int:pk>/update/',
         DetailsUpdateView.as_view(), name='details-update'),
    path('details/<int:pk>/delete/',
         DetailsDeleteView.as_view(), name='details-delete'),

    # Task URLs
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    # ProjectIssues URLs
    path('project-issues/', ProjectIssuesListView.as_view(), name='project-issues-list'),
    path('project-issues/create/', ProjectIssuesCreateView.as_view(), name='project-issues-create'),
    path('project-issues/<int:pk>/', ProjectIssuesDetailView.as_view(), name='project-issues-detail'),
    path('project-issues/<int:pk>/update/', ProjectIssuesUpdateView.as_view(), name='project-issues-update'),
    path('project-issues/<int:pk>/delete/', ProjectIssuesDeleteView.as_view(), name='project-issues-delete'),
]
