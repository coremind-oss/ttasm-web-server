from django.contrib import admin
from django.contrib.auth.models import User

from data.models import Desktop
from data.models import Android
from data.models import Client_Key_Hash




# Register your models here.
admin.site.register(Desktop)
admin.site.register(Android)
admin.site.register(Client_Key_Hash)
