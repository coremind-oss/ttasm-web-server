from django.db import models
from os import name

# Create your models here.
class Desktop(models.Model):
    name = models.CharField(max_length = 255)
    datetime_registered = models.DateTimeField(auto_now_add=True)
    