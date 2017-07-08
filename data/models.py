from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields.jsonb import JSONField
from django.db.models.fields.related import ForeignKey


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
    base_date = models.DateField()
    data = JSONField(default=[])
    user = ForeignKey(User)
    
    def __str__(self):
        return "This is DailyActivity for user: {} with data: {}".format(self.user, self.data)
        