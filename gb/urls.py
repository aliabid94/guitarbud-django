from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getsongs/(?P<searchstring>[A-Za-z0-9# _-]+)/$', views.getsongs, name='getsongs'),    
    url(r'^tab/(?P<tab_url>[\.A-Za-z0-9# _-]+)/$', views.gettab, name='gettab'),    
    url(r'^search/(?P<searchstring>[\.A-Za-z0-9# _-]+)/$', views.getsearch, name='getsearch'),    
    url(r'^audio/(?P<note>[\.A-Za-z0-9# _-]+)/$', views.playAudioFile, name='playAudioFile'),    
    url(r'^random/$', views.random, name='random'),    
]