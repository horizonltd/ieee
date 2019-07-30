from django.db import models
from conference.models import Conference

# Create your models here.
# Models
class Downloads(models.Model):
    File_Title = models.CharField(max_length=200, default='')
    File = models.FileField(upload_to='materials/')
    Author = models.CharField(max_length=200, default='')
    File_Description = models.TextField(max_length=200, default='')
    Year = models.DateField(default=2019-12-13)
    Conference = models.ForeignKey(Conference, related_name='conf', on_delete=models.CASCADE, default='')
    # default=2019-12-13

    def __str__(self):

        return self.File_Title

