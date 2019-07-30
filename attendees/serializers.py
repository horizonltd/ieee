from rest_framework import serializers
#from hub.models import Lecture
from .import models

class TypeOfMembershipSerializer(serializers.ModelSerializer):
    
    Member_Entry = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.TypeOfMembership
        # fields = '__all__'
        fields = ('Membership_Type','Member_Entry')