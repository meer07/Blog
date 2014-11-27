__author__ = 'naoya-kaige'
from django.conf.urls import patterns, url
from cms import views

urlpatterns = patterns('',
url(r'^blog/$', views.blog_list, name='blog_list'),
url(r'^blog/search$', views.tag_seach, name='tag_search'),)