from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ba.urls')),
    path('', include('webservice.urls')),
    path('', include('projects.urls')),
    path('', include('auth_module.urls')),
]
 