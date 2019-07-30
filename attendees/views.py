from rest_framework import generics
from . import models
from . import serializers

#Event views
class TypeOfMembershipList(generics.ListCreateAPIView):
    queryset  = models.TypeOfMembership.objects.all()
    serializer_class = serializers.TypeOfMembershipSerializer
    
class TypeOfMembershipDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TypeOfMembership.objects.all()
    serializer_class = serializers.TypeOfMembershipSerializer

