# from django.contrib.auth.models import User
from django.db import models
# from django.conf import settings
from cloudinary.models import CloudinaryField
from auths.models import CustomUser
from clients.models import Client


class Project(models.Model):
    """project model schema

    Args:
        models (_type_): project model
    """
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('completed', 'completed'),
        ('inprogress', 'inprogress'),
        ('terminated', 'terminated'),
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='pending')
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="projects",
        null=True,
        blank=True
    )
    contractor = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE, 
        related_name="contractor_projects",
        null=True,
        blank=True
    )
    document = CloudinaryField('document', resource_type='raw', blank=True, null=True)
    working_time = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    parent_project = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='sub_projects',
        blank=True,
        null=True
    )

    # example usage
    # parent_project = Project.objects.create(
    # name="Parent Project", manager=some_user)
    # sub_project = Project.objects.create(
    # name="Sub Project", manager=some_user,
    # parent_project=parent_project)

    def __str__(self):
        return f'Project: {self.name}'


class WorkSchedule(models.Model):
    """Work Schedule model schema

    Args:
        models (_type_): work schedule model
    """
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="work_schedules"
    )
    working_manager = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE, 
        related_name="working_manager"
    )
    hours_per_week = models.TimeField()
    working_time = models.TimeField()
    day_of_the_week = models.CharField(max_length=10)
    work_from = models.TimeField()
    work_to = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Work Schedule for {self.project.name}'


class Details(models.Model):
    """Details model schema

    Args:
        models (_type_): details model
    """
    id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="details"
    )
    project_manager = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="details_project_manager"
    )
    head_of_project = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE, 
        related_name="project_head"
    )
    sub_project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="sub_project_details",
        blank=True,
        null=True
    )
    sub_contractor = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="subcontractor_projects",
        blank=True, 
        null=True
    )
    
    boq = models.ForeignKey(
        "bill_of_quantity.BillOfQuantity",
        on_delete=models.CASCADE,
        related_name="details",
        blank=True, 
        null=True,
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Details for {self.projectId.name}'


class Task(models.Model):
    """task schema"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    material_requisition = models.CharField(max_length=150)
    material_consumed = models.CharField(max_length=150)
    material_planning = models.CharField(max_length=150)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project'
    )

    assigned_to = models.ForeignKey(
        CustomUser,
        related_name='assigned_tasks',
        on_delete=models.CASCADE
    )
    hours_planned = models.DateTimeField()
    stage = models.TextField()
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Task: {self.name}'
    

class ProjectIssues(models.Model):
    """Task Issues
      for problems associated to a project
    """
    STATUS_CHOICES = [
        ('assigned', 'assigned'),
        ('unassigned', 'unassigned'),
        ('completed', 'completed')
    ]
    id = models.AutoField(primary_key=True)
    projectId = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='timesheets'
    )
    task_id = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="tasks_issues"
    )
    created = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=100)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='unassigned')

# class ProjectOperation(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('completed', 'Completed'),
#     ]
#     project = models.OneToOneField(
#         Project,
#         on_delete=models.CASCADE,
#         related_name="operations"
#     )
#     status = models.CharField(max_length=20,
#                               choices=STATUS_CHOICES,
#                               default='pending')
#     design_document_url = models.URLField()
#     milestones = models.ManyToManyField(
#         'Milestone',
#         related_name="project_operations",
#         null=True,
#         blank=True
#     )
#     progress_report = models.TextField()

#     def __str__(self):
#         return f'Operations for Project: {self.project.name}'


# class Milestone(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#     date = models.DateField()
#     completed = models.BooleanField(default=False)
#     project = models.ForeignKey(Project,
#                                 on_delete=models.CASCADE,
#                                 related_name="milestones")

#     def __str__(self):
#         return f'Milestone: {self.name}'


# class Timesheet(models.Model):
#     """time sheet for a project"""
#     project = models.ForeignKey(
#         Project,
#         on_delete=models.CASCADE,
#         related_name='timesheets')
#     created_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="timesheet_manager"
#     )
#     hours_per_week = models.PositiveIntegerField()
#     working_time = models.TimeField()
#     DAY_OF_WEEK_CHOICES = [
#         ('monday', 'Monday'),
#         ('tuesday', 'Tuesday'),
#         ('wednesday', 'Wednesday'),
#         ('thursday', 'Thursday'),
#         ('friday', 'Friday'),
#         ('saturday', 'Saturday'),
#         ('sunday', 'Sunday'),
#     ]
#     day_of_week = models.CharField(max_length=9, choices=DAY_OF_WEEK_CHOICES)
#     work_from = models.TimeField()
#     work_to = models.TimeField()
#     start_date = models.DateField()
#     end_date = models.DateField()

#     def __str__(self):
#         return f'Timesheet for {self.project.name}'
