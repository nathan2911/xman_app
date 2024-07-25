from django.urls import path, include
from . import views

urlpatterns = [
    path('ba', views.ba, name='ba'),
    path('val/api/v1', views.ba_web_service, name='ba_web_service'),
    path('rec/api-v1', views.questionnaire, name='questionnaire'),
]