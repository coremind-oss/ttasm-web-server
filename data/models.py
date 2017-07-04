from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.postgres.fields.jsonb import JSONField
from idlelib.IOBinding import blank_re
from django.db.models.fields.related import ForeignKey

#Create your models here.
class Desktop(models.Model):
    datetime_registered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    public_key = models.TextField(null=True, blank=True)
    uuid = models.CharField(max_length=64, null=True, blank=True)
    token = models.CharField(max_length=64, null=True, blank=True)
 
class Android(models.Model):
    datetime_registered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    desktop = models.ForeignKey(Desktop)

class DailyActivity(models.Model):
    data = JSONField(blank=True, null=True)# we're not sure if there is a limitation in JSONFiled length
    user = ForeignKey(User)
    