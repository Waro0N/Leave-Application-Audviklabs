from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User



types_of_leaves = (
    ('Sick Leave', 'Sick Leave'),
    ('Earned Leave', 'Earned Leave'),
    ('Annual Leave', 'Annual Leave'),
)   
# Create your models here.
class LeaveApp(models.Model):
    fdate = models.DateField()
    tdate=models.DateField()
    type_of_leave=models.CharField(max_length=20 ,choices =types_of_leaves, default = "" )
    reason = models.CharField(max_length=500)
    authuser = models.ForeignKey(User, on_delete=models.CASCADE,default = '', null =True)
    
    def __str__(self):
        return self.reason


class Sick_leave(models.Model):
    leave=models.CharField(max_length = 40)

    def __str__(self):
        return self.leave