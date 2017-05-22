from django.conf.urls import url, include
from django.contrib import admin

from ui import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^reverse_link$', views.reverse_link,name='reverse_link'),
#         url(r'^inactivity$',views.inactivity, name='inactivity'),
        url(r'^logout_page/$', views.logout_page,name='logout_page'),
        url(r'^desktop_router/$', views.desktop_router, name='desktop_router'),
        url(r'^download_page/$', views.download_page, name='download_page')
        
        
]
