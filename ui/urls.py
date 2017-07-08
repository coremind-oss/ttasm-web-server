from django.conf.urls import url

from ui import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^inactivity_logout/$', views.showing_reverse, name='showing_reverse'),
    
    # DESKTOP COMMS
    url(r'desktop-login', views.desktop_login, name='desktop_login'),
    url(r'^public_key/$', views.public_key, name='public_key'),
    url(r'^timestamp_message_handling/$', views.timestamp_message_handling, name='timestamp_message_handling'),
    
    
    # USER PROFILE
    url(r'^accounts/profile/$', views.profile, name='profile'),
]
