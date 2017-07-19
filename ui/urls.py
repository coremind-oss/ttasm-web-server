from django.conf.urls import url

from ui import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^inactivity_logout/$', views.showing_reverse, name='showing_reverse'),
    
    # DESKTOP COMMS
    url(r'^public_key/$', views.public_key, name='public_key'),
    url(r'^initial_synchronization/$', views.initial_synchronization, name='initial_synchronization'),

    # TIMESTAMP VIEWS
    url(r'^timestamp_message_handling/$', views.timestamp_message_handling, name='timestamp_message_handling'),
    url(r'^last_activity_duration/$', views.last_activity_duration, name='last_activity_duration'),
    
    # USER PROFILE
    url(r'^accounts/profile/$', views.profile, name='profile'),

]
