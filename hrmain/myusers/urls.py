from django.contrib import admin
from django.urls import path
from django import views
from django.urls import include
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]