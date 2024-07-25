from django.urls import path, include
from .views import ListRecords, DetailRecords, FetchBA

urlpatterns = [
    path('api/v1/', ListRecords.as_view()),
    path('<int:pk>/', DetailRecords.as_view()),
    path('ba/api/v1', FetchBA.as_view())
]