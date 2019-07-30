from rest_framework import serializers
#from hub.models import Lecture
from .import models
#from conference.serializers import ConferenceSerializer

# Serializers
class OtherSerializer(serializers.ModelSerializer):

    #event = ConferenceSerializer(many=True)
    #conference_title = serializers.CharField(write_only=True, required=False)
    #Member_Entry = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Other
        fields = ('File_Title','File')