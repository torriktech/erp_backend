# Register your models here.
"""admin model regs"""
from django.contrib import admin
from .models import Appraisal, Payroll

admin.site.register(Appraisal)
admin.site.register(Payroll)
