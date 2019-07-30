from rest_framework import generics
from . import models
from . import serializers

#Event views
class ConferenceList(generics.ListCreateAPIView):
    queryset  = models.Conference.objects.all()
    serializer_class = serializers.ConferenceSerializer
    
class ConferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Conference.objects.all()
    serializer_class = serializers.ConferenceSerializer

