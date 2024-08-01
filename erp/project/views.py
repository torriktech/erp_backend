from rest_framework import generics
from .models import Project, WorkSchedule, Details, Task, ProjectIssues
from .serializers import ProjectSerializer, WorkScheduleSerializer, DetailsSerializer, TaskSerializer, ProjectIssuesSerializer


class ProjectListView(generics.ListAPIView):
    """
    List all projects.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectCreateView(generics.CreateAPIView):
    """
    Create a new project.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single project instance.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectUpdateView(generics.UpdateAPIView):
    """
    Update a project instance.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDeleteView(generics.DestroyAPIView):
    """
    Delete a project instance.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# WorkSchedule Views
class WorkScheduleListView(generics.ListAPIView):
    """
    List all work schedules.
    """
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer


class WorkScheduleCreateView(generics.CreateAPIView):
    """
    Create a new work schedule.
    """
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer


class WorkScheduleDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single work schedule instance.
    """
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer


class WorkScheduleUpdateView(generics.UpdateAPIView):
    """
    Update a work schedule instance.
    """
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer


class WorkScheduleDeleteView(generics.DestroyAPIView):
    """
    Delete a work schedule instance.
    """
    queryset = WorkSchedule.objects.all()
    serializer_class = WorkScheduleSerializer


# Details Views
class DetailsListView(generics.ListAPIView):
    """
    List all details.
    """
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer


class DetailsCreateView(generics.CreateAPIView):
    """
    Create new details.
    """
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer


class DetailsDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single details instance.
    """
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer


class DetailsUpdateView(generics.UpdateAPIView):
    """
    Update a details instance.
    """
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer


class DetailsDeleteView(generics.DestroyAPIView):
    """
    Delete a details instance.
    """
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer


class DetailsListByProjectView(generics.ListAPIView):
    """
    View to list details based on project ID.
    """
    serializer_class = DetailsSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Details.objects.filter(project_id=project_id)


# Task Views
class TaskListView(generics.ListAPIView):
    """
    List all tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateView(generics.CreateAPIView):
    """
    Create a new task.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single task instance.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateView(generics.UpdateAPIView):
    """
    Update a task instance.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDeleteView(generics.DestroyAPIView):
    """
    Delete a task instance.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListByProjectView(generics.ListAPIView):
    """
    View to list tasks based on project ID.
    """
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return Task.objects.filter(project=project_id)
    

# ProjectIssues Views
class ProjectIssuesListView(generics.ListAPIView):
    """
    List all project issues.
    """
    queryset = ProjectIssues.objects.all()
    serializer_class = ProjectIssuesSerializer


class ProjectIssuesCreateView(generics.CreateAPIView):
    """
    Create a new project issue.
    """
    queryset = ProjectIssues.objects.all()
    serializer_class = ProjectIssuesSerializer


class ProjectIssuesDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single project issue instance.
    """
    queryset = ProjectIssues.objects.all()
    serializer_class = ProjectIssuesSerializer


class ProjectIssuesUpdateView(generics.UpdateAPIView):
    """
    Update a project issue instance.
    """
    queryset = ProjectIssues.objects.all()
    serializer_class = ProjectIssuesSerializer


class ProjectIssuesDeleteView(generics.DestroyAPIView):
    """
    Delete a project issue instance.
    """
    queryset = ProjectIssues.objects.all()
    serializer_class = ProjectIssuesSerializer
