from email import message
from django.shortcuts import render , redirect
import os
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect, FileResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .forms import LeaveAppform

from .models import LeaveApp



# Create your views here.




def login_view(request):
    if request.method=='POST':
        
        loginusername = request.POST['lusername']
        loginpassword = request.POST['lpass']
        user = authenticate(request, username = loginusername, password = loginpassword)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'This User is not existed in our database, Please enter a valid user id')
            return redirect('login') 
    
        
    return render(request, 'accounts/login.html') 


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    if request.method == 'POST':
        
        form = LeaveAppform(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['reason']
            fdate = form.cleaned_data['fdate']
            tdate = form.cleaned_data['tdate']
            type_of_leave=form.cleaned_data['type_of_leave']
            
        myreq= LeaveApp(reason = reason, fdate = fdate, tdate=tdate, type_of_leave=type_of_leave)
        myreq.save()
    
    form = LeaveAppform()
    params ={'form' : form}

    return render(request, 'accounts/leaveindex.html', params)


@login_required
def leave_status(request):
    leavedata=LeaveApp.objects.all()
    page= request.GET.get('page', 1)
    paginator = Paginator(leavedata,5)
    try:
        page_obj=paginator.get_page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj=paginator.page(paginator.num_pages)
        
    
    params = {'page_obj':page_obj}
    return render(request, 'accounts/leavestatus.html', params)


@login_required
def calender_view(request):
    return render(request, 'accounts/calender.html')