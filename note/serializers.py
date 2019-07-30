from rest_framework import serializers
#from hub.models import Lecture
from .import models

# Serializers
class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallery
        fields = ('Title','File')

