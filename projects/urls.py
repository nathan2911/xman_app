from django.urls import path, include
from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('dashboard/', views.dashboard, name='dashboard'),
    ]