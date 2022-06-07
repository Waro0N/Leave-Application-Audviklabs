from django.contrib import admin
from .models import LeaveApp, Sick_leave
# Register your models here.
admin.site.register(LeaveApp)
admin.site.register(Sick_leave)