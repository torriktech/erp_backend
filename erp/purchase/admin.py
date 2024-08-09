from django.contrib import admin
from .models import Requisition, PurchaseOrder, RequisitionItem 
# Register your models here.

admin.site.register(Requisition)
admin.site.register(RequisitionItem)
admin.site.register(PurchaseOrder)
