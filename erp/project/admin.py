"""admin model regs"""
from django.contrib import admin
from .models import WorkSchedule, ProjectIssues, Project, Details

admin.site.register(Project)
admin.site.register(ProjectIssues)
admin.site.register(Details)
admin.site.register(WorkSchedule)
