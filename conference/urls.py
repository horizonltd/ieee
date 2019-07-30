from django.urls import path
from . import views
#from django.conf.urls.static import static
#from django.conf import settings

#This bind the views created in views.py class of the hub
urlpatterns = [


    #Event
    path('', views.ConferenceList.as_view()),
    path('<int:pk>/', views.ConferenceDetail.as_view()), #This get the ID of the passed lecture
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
