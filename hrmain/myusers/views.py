from email import message
from django.shortcuts import render , redirect
import os
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect, FileResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from . import models

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
    
        
    return render(request, 'myusers/login.html') 


def logout_view(request):
    logout(request)
    return redirect('login')
    