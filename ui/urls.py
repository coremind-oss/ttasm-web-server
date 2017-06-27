from django.conf.urls import url

from ui import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^inactivity_logout/$', views.showing_reverse, name='showing_reverse'),
    
    # DESKTOP COMMS
    url(r'desktop-login', views.desktop_login, name='desktop_login'),
    url(r'^public_key/$', views.public_key, name='public_key'),
    url(r'^public_key/(?P<pub_key_hash>[0-9A-Za-z]+)/$', views.public_key, name='public_key'),
#     url(r'^client_key_hash/$', views.client_key_hash, name='client_key_hash'),
#     url(r'^client_key_hash/(?P<client_key_hash>[0-9A-Za-z]+)/$', views.client_key_hash, name='client_key_hash'),
#     url(r'^client_key/$', views.client_key, name='client_key'),
#     url(r'^client_key/(?P<client_key>[0-9A-Za-z]+)/$', views.client_key, name='client_key'),
#     url(r'^auth/$', views.auth, name='auth'),
    
    # USER PROFILE
    url(r'^accounts/profile/$', views.profile, name='profile'),
]
