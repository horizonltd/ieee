from django.db import models
from conference.models import Conference
# Create your models here.


class AGM(models.Model):
    title = models.CharField(max_length=200, default='')
    file = models.FileField(upload_to='materials/')
    file_description = models.TextField(max_length=200, default='')
    year = models.DateField(default=2019-12-13)
    conference = models.ForeignKey(Conference, related_name='agm_conf', on_delete=models.CASCADE, default='')

    def __str__(self):

        return self.title
