from django.conf.urls import url

from ui import views


urlpatterns = [
#     url(r'^$', views.index, name='index'),
    url(r'^inactivity_logout/$', views.showing_reverse, name='showing_reverse'),
    
    # DESKTOP COMMS
    url(r'^desktop_router/$', views.desktop_router, name='desktop_router'),
    
    
    
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^sign_out/$', views.sign_out, name='sign_out'),
    url(r'^index/$', views.index, name='index')
]
