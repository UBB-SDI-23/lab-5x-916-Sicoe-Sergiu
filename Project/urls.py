
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('Project.dj.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
