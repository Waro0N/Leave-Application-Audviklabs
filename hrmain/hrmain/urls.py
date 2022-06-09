from django.contrib import admin
from django.urls import path
from django import views
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('login/', include('myusers.urls')),
]