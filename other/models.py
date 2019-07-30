from django.db import models
# Create your models here.
# Models
class Other(models.Model):
    File_Title = models.CharField(max_length=200, default='')
    File = models.FileField(upload_to='materials/')
    # default=2019-12-13

    def __str__(self):

        return self.File_Title
