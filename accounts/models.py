from django.db import models
from django.contrib import auth
from django.forms import forms
from django.forms import TextInput, Textarea
from django.contrib.auth.models import AbstractUser
# Create your models here.

#This is a predefined django function, for user login and authentication
class User(auth.models.User, auth.models.PermissionsMixin):
    # Registration_Number = models.CharField(max_length=200, default=True) # True for male and False for female
    # Token = models.CharField(max_length=200, default=True) # True for male and False for female

    #Automically set the a form for the user make it to DB
    def __str__(self):
        return "@{}".format(self.username)