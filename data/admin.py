from django.contrib import admin

from data.models import Desktop
from data.models import Android
from data.models import DailyActivity


# Register your models here.
admin.site.register(Desktop)
admin.site.register(Android)
admin.site.register(DailyActivity)

