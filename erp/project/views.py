"""project management controller"""
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Project, ProjectOperation, Task, Milestone
from .serializers import (
    ProjectSerializer,
    ProjectOperationSerializer,
    TaskSerializer,
    MilestoneSerializer
)

    
class ProjectListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing all projects or creating a new project.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a specific project.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectOperationCreateAPIView(generics.CreateAPIView):
    """
    API view for creating a new project operation.
    """
    serializer_class = ProjectOperationSerializer

    def perform_create(self, serializer):
        project_id = self.request.data.get('project_id')
        project = Project.objects.get(id=project_id)
        serializer.save(project=project)


class ProjectOperationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a specific project operation.
    """
    queryset = ProjectOperation.objects.all()
    serializer_class = ProjectOperationSerializer


class TaskListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing all tasks or creating a new task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a specific task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class MilestoneListCreateAPIView(generics.ListCreateAPIView):
    """
    API view for listing all milestones or creating a new milestone.
    """
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer


class MilestoneDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a specific milestone.
    """
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer
