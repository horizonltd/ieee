from rest_framework import generics
from . import models
from . import serializers
from rest_framework.response import Response
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
#from resources.models import Other





def advice(request):
    template = loader.get_template('advice.html')
    context = {
        'downloads': Other.objects.all()

    }
    return HttpResponse(template.render(context, request))



class OtherList(generics.ListCreateAPIView):
    queryset  = models.Other.objects.all()
    serializer_class = serializers.OtherSerializer
class OtherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Other.objects.all()
    serializer_class = serializers.OtherSerializer