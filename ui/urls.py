from django.conf.urls import url

from ui import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^showing_reverse/$', views.showing_reverse, name='showing_reverse'),
]
