from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('on-progress', 'On Progress'),
    ]

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='pending')
    manager = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name="managed_projects")
    document = models.FileField(upload_to='attachments/')
    client_name = models.CharField(max_length=100)
    working_time = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'Project: {self.name}'


class ProjectOperation(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="operations")
    sites = models.CharField(max_length=200)
    milestones = models.ManyToManyField('Milestone', related_name="project_operations")
    progress_report = models.TextField()

    def __str__(self):
        return f'Operations for Project: {self.project.name}'


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    material_requisition = models.CharField(max_length=150)
    material_consumed = models.CharField(max_length=150)
    material_planning = models.CharField(max_length=150)
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name="tasks")
    assigned_to = models.ManyToManyField(User, related_name="assigned_tasks")
    client_name = models.CharField(max_length=100)
    hours_planned = models.DateTimeField()
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Task: {self.name}'


class Milestone(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name="milestones")

    def __str__(self):
        return f'Milestone: {self.name}'

