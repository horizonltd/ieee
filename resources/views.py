from rest_framework import generics
from . import models
from . import serializers
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from resources.models import Downloads





def advice(request):
    template = loader.get_template('advice.html')
    context = {
        'downloads': Downloads.objects.all()

    }
    return HttpResponse(template.render(context, request))



class DownloadsList(generics.ListCreateAPIView):
    queryset  = models.Downloads.objects.all()
    serializer_class = serializers.DownloadsSerializer
class DownloadsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Downloads.objects.all()
    serializer_class = serializers.DownloadsSerializer