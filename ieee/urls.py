
from django.contrib import admin
from django.urls import path, include
from .views import login
from . import views
from django.conf.urls.static import static
from django.conf import settings

# from .views import login, sample_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/conference/', include('conference.urls')),
    path('api/login', login),
    path('api/attendees/', include('attendees.urls')),
    path('api/gallery/', include('note.urls')),
    # path('api/sampleapi', sample_api),
    path('api/resources/', include('resources.urls')),
    path('api/agm/', include('agm.urls')),
    path('api/other/', include('other.urls')),


    # path('api/sampleapi', sample_api),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    path('test/', views.TestPage.as_view(), name='test'),
    path('advice/', views.Advice.as_view(), name='advice'),
]

#This help you to view file on media folder created by django
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)