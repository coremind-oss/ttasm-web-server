from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

#Create your models here.
class Desktop(models.Model):
    datetime_registered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    public_key = models.TextField(null=True, blank=True)
 
class Android(models.Model):
    datetime_registered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    desktop = models.ForeignKey(Desktop)
