from .models import LeaveApp, Sick_leave
from django import forms
from django.contrib.auth.models import User



class LeaveAppform(forms.ModelForm):
    fdate = forms.DateField(label ='From date:', widget=forms.DateInput(attrs={'class': 'form-control', 'name': 'fdate', 'id': 'fdate', 'data-date-format':'yyyy-mm-dd', 'placeholder': 'YYYY-MM-DD' ,'type': 'date'}))

    tdate = forms.DateField(label ='To date:', widget=forms.DateInput(attrs={'class': 'form-control', 'name': 'tdate', 'id': 'tdate', 'data-date-format':'yyyy-mm-dd', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}))
    
    type_of_leave = forms.ModelChoiceField(queryset = Sick_leave.objects.all().distinct(),label='Type of Leave', widget=forms.Select(attrs={'class' : 'form-control', 'name': 'ltype', 'id': 'ltype'}))
    
    reason = forms.CharField(label='Reason' ,widget= forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Write your Reason'}))

    class Meta:
        model = LeaveApp
        fields = ('fdate', 'tdate', 'type_of_leave', 'reason')
        