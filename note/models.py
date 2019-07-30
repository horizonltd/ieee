from django.db import models
from  attendees.models import Members
from  attendees.models import Members

# Create your models here.
# Models
class Gallery(models.Model):
    Title = models.CharField(max_length=200, default='')
    File = models.FileField(upload_to='materials/', default='')
    # default=2019-12-13

    def __str__(self):

        return self.Title

