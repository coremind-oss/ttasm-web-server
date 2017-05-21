from django.db import models
from os import name
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Desktop(models.Model):
    name = models.CharField(max_length = 255)
    datetime_registered = models.DateTimeField(auto_now_add=True)
    
class Android(models.Model):
    name = models.CharField(max_length = 255)
    datetime_registered = models.DateTimeField(auto_now_add=True)
    desktop = models.ForeignKey('Desktop')
    