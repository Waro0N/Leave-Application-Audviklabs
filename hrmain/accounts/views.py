from email import message
from django.shortcuts import render , redirect
import os
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect, FileResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .forms import LeaveAppform
from . import models
from .models import LeaveApp



# Create your views here.
@login_required
def dashboard(request):
    if request.method == 'POST':
        
        form = LeaveAppform(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            fdate = form.cleaned_data['fdate']
            tdate = form.cleaned_data['tdate']
            type_of_leave=form.cleaned_data['type_of_leave']
            
        myreq= LeaveApp(authuser = request.user, reason = reason, fdate = fdate, tdate=tdate, type_of_leave=type_of_leave)
        myreq.save()
    
    form = LeaveAppform()
    params ={'form' : form}

    return render(request, 'accounts/leaveindex.html', params)


@login_required
def leave_status(request):
    
    leavedata=LeaveApp.objects.filter(authuser=request.user)
    
    
    params = {'leavedata':leavedata}
    return render(request, 'accounts/leavestatus.html', params)


@login_required
def calender_view(request):
    return render(request, 'accounts/calender.html')