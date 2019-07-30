from rest_framework import serializers
#from hub.models import Lecture
from .import models



class IconSerializer(serializers.ModelSerializer):

    #event = ConferenceSerializer(many=True)
    class Meta:

        model = models.Icon
        fields = '__all__'
        #fields = ('Icon_Group')


#Correction Point Above
class AgendaSerializer(serializers.ModelSerializer):


    #icon = IconSerializer(many=True)
    #event = ConferenceSerializer(many=True)


    class Meta:

        model = models.Agenda
        #fields = '__all__'
        fields = ('Day','Event','Title','Remarks','Start_Time','End_Time','Date','Agenda_Icon')



class ConferenceSerializer(serializers.ModelSerializer):

    #agendas = serializers.StringRelatedField(many=True)
    agendas = AgendaSerializer(many=True)

    class Meta:

        model = models.Conference
        #depth=1
        # fields = '__all__'
        fields = ('id','conference_paper', 'conference_title', 'upload_paper','proceeding_paper_title','author','speaker_name','other_authors',
        'conference_location','sponsor',
        'conference_start_date',
        'conference_end_date','place_of_publication','online_link','latitude','cover_image','futured_image','members_fee','non_members_fee','longitude','event_link','agendas')
