from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.fields import DateTimeField
from django.contrib.postgres.fields.jsonb import JSONField

#Create your models here.
class Desktop(models.Model):
    datetime_registered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    public_key = models.TextField(null=True, blank=True)
    uuid = models.CharField(max_length=64, null=True, blank=True)
    token = models.CharField(max_length=64, null=True, blank=True)
    user = models.ForeignKey(User)
    timezone = models.CharField(max_length=32)
 
class Android(models.Model):
    datetime_registered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    desktop = models.ForeignKey(Desktop)

class DailyActivity(models.Model):
    timestamp = JSONField(default=[])
    user = models.ForeignKey(User)
    base_date = models.DateField(auto_now=True)