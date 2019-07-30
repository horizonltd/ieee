from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


#Type of Membership
class TypeOfMembership(models.Model):
    Membership_Type = models.CharField(max_length=150)

    def __str__(self):
        return self.Membership_Type

class Members(models.Model):
    membership_registration_number = models.CharField(max_length=150, default='')
    Full_Name = models.CharField(max_length=150, default='')
    address	= models.TextField(max_length=200, default='')
    phone_number = models.IntegerField(default='')
    email = models.EmailField()
    Payment_status = models.CharField(max_length=50, default='')
    entry_types = models.ForeignKey(TypeOfMembership, related_name='Member_Entry', on_delete=models.CASCADE, default='')

    #class Meta:
        #unique_together = ('membership_registration_number', 'phone_number')
        #ordering = ['phone_number']

    def __str__(self):
        return self.Full_Name
        #return '%d: %s' % (self.phone_number, self.membership_registration_number)


