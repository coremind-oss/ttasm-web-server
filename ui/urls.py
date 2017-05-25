from django.conf.urls import url

from ui import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^inactivity_logout/$', views.showing_reverse, name='showing_reverse'),
    
    # DESKTOP COMMS
    url(r'^desktop_router/$', views.desktop_router, name='desktop_router'),
    url(r'^register/$',views.register,name='register')
]
