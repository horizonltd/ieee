from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify



class Icon(models.Model):
    File = models.FileField()
    Icon_Group = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.Icon_Group

#Event Model
class Conference(models.Model):
    conference_paper = models.CharField(max_length=100, default='')
    conference_title = models.CharField(max_length=100, default='')
    upload_paper = models.FileField()
    proceeding_paper_title = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    speaker_name = models.CharField(max_length=100, default='')
    other_authors = models.CharField(max_length=100, default='')
    conference_location = models.CharField(max_length=100, default='')
    sponsor = models.CharField(max_length=100, default='')
    conference_start_date = models.DateField(default=2019-12-13)
    conference_end_date = models.DateField(default=2019-12-13)
    place_of_publication = models.CharField(blank=True, max_length=100)
    online_link = models.URLField(default='')
    cover_image = models.ImageField(default='')
    futured_image = models.ImageField(default='')
    members_fee = models.CharField(max_length=100, default='')
    non_members_fee = models.CharField(max_length=100, default='')
    event_link = models.URLField(default='')
    latitude = models.CharField(max_length=150, default='')
    longitude = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.conference_paper


#AGENDA REQUIREMENTS
class Agenda(models.Model):
    Day = models.IntegerField(default='', blank=True)
    Event = models.ForeignKey(Conference, related_name='agendas', on_delete=models.CASCADE, default='')
    Title = models.CharField(max_length=255)
    Remarks = models.CharField(max_length=255, default='', blank=True)
    Start_Time = models.TimeField(default=6.51)
    End_Time = models.TimeField(default=2019-6-26)
    Date = models.DateField(default=6.51)
    Agenda_Icon = models.ForeignKey(Icon, related_name='icon_file', on_delete=models.CASCADE, default='')


    class Meta:
        unique_together = ('Title', 'Day')
        ordering = ['Day']

    def __str__(self):
        return '%d: %s' % (self.Day, self.Title)


