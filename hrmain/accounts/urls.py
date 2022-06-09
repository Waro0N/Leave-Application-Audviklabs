from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('leavestatus/', views.leave_status, name='leavestatus'),
    path('calender/', views.calender_view, name='calender'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)