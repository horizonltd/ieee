from django.urls import path
from . import views

#This bind the views created in views.py class of the hub
# 
urlpatterns = [
    path('', views.DownloadsList.as_view()),
    path('<int:pk>/', views.DownloadsDetail.as_view()), #This get the ID of the passed lecture

]
