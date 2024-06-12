# from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Project(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('on-progress', 'On-Progress'),
    ]

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='pending')
    manager = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="project_manager")
    document = models.FileField(upload_to='attachments/')
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='client_projects',
        blank=True,
        null=True
    )
    working_time = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    parent_project = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='sub_projects',
        blank=True,
        null=True
    )
    budget = models.CharField(max_length=255, blank=True, null=True)
    
    # example usage
    # parent_project = Project.objects.create(
    # name="Parent Project", manager=some_user)
    # sub_project = Project.objects.create(
    # name="Sub Project", manager=some_user,
    # parent_project=parent_project)
 
    def __str__(self):
        return f'Project: {self.name}'


class ProjectOperation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        related_name="operations"
    )
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='pending')
    design_document = models.FileField(upload_to='attachments/')
    milestones = models.ManyToManyField(
        'Milestone',
        related_name="project_operations",
        null=True,
        blank=True
    )
    progress_report = models.TextField()

    def __str__(self):
        return f'Operations for Project: {self.project.name}'


class Task(models.Model):
    """task schema"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    material_requisition = models.CharField(max_length=150)
    material_consumed = models.CharField(max_length=150)
    material_planning = models.CharField(max_length=150)
    project_operations = models.ForeignKey(
        ProjectOperation,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    assigned_to = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="assigned_tasks"
    )
    hours_planned = models.DateTimeField()
    stage = models.TextField()
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


class Timesheet(models.Model):
    """time sheet for a project"""
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='timesheets')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="timesheet_manager"
    )
    hours_per_week = models.PositiveIntegerField()
    working_time = models.TimeField()
    DAY_OF_WEEK_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    day_of_week = models.CharField(max_length=9, choices=DAY_OF_WEEK_CHOICES)
    work_from = models.TimeField()
    work_to = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Timesheet for {self.project.name}'
    