from django.contrib import admin

from data.models import Desktop
from data.models import Android
from data.models import DailyActivity

# Register your models here.

class AdminDesktop(admin.ModelAdmin):
    list_display = ['name','uuid' ,'datetime_registered']
    class Meta:    
        model = Desktop
        
class AdminAndroid(admin.ModelAdmin):
    list_display = ['name', 'desktop']
    class Meta:
        model = Android

class AdminDailyActivity(admin.ModelAdmin):
    list_display = ['user','base_date','data']
    list_filter = ['user', 'base_date']
    class Meta:
        model = DailyActivity
    
admin.site.register(Desktop, AdminDesktop)
admin.site.register(Android, AdminAndroid)
admin.site.register(DailyActivity, AdminDailyActivity)
