from django.contrib import admin
from .models import CustomUser, CompanyProfile, Employee

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(CompanyProfile)
admin.site.register(Employee)
