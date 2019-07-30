from rest_framework import generics
from . import models
from . import serializers

#Event views
class GalleryList(generics.ListCreateAPIView):
    queryset  = models.Gallery.objects.all()
    serializer_class = serializers.GallerySerializer
class GalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Gallery.objects.all()
    serializer_class = serializers.GallerySerializer