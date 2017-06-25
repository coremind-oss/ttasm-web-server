from django.db import models
from django.contrib.auth.models import User

#Create your models here.
class Desktop(models.Model):
    datetime_registered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
 
class Android(models.Model):
    datetime_registered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    desktop = models.ForeignKey(Desktop)
 
class Client_Key(models.Model):
    pub_key = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    def __str__(self):
        return self.pub_key

# class Client_Key_Hash(models.Model):
#     key_hash = models.CharField(max_length=255)
#     user = models.ForeignKey(User)
#     def __str__(self):
#         return self.key_hash