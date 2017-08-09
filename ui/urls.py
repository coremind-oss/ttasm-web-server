from django.conf.urls import url
from ui import views


# from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^inactivity_logout/$', views.inactivity_logout, name='inactivity_logout'),
    
    # DESKTOP COMMS
    url(r'^public_key/$', views.public_key, name='public_key'),
    url(r'^initial_synchronization/$', views.initial_synchronization, name='initial_synchronization'),

    # TIMESTAMP VIEWS
    url(r'^timestamp_message_handling/$', views.timestamp_message_handling, name='timestamp_message_handling'),
    url(r'^last_activity_duration/$', views.last_activity_duration, name='last_activity_duration'),
    url(r'^get_daily_activities/$', views.get_daily_activities, name='get_daily_activities'),
    
    
    # USER PROFILE
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
#     url(r'^accounts/logout/$', views.logout, name='logout'),


    


]
