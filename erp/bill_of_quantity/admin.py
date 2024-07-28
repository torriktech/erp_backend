# admin register key and BOQ
from django.contrib import admin
from .models import Key, BillOfQuantity
# Register your models here.

admin.site.register(Key)
admin.site.register(BillOfQuantity)
