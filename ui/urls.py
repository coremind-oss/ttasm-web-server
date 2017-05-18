
from django.conf.urls import url, include
from django.contrib import admin

from ui import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^reverse_link$', views.reverse_link,name='reverse_link'),
]
