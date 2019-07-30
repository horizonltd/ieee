from rest_framework import serializers
#from hub.models import Lecture
from .import models

# Serializers
class AGMSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AGM
        fields = ('id','title','file','file_description','conference','year')