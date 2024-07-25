from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('user_logout/', views.user_logout, name='user_logout'),
]