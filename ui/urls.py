from django.conf.urls import url

from ui import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # all other urls come in between
    
    # catch all url
    url(r'^.*$', views.catch_all, name='catch_all'),
]
