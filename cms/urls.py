__author__ = 'naoya-kaige'
from django.conf.urls import patterns, url
from cms import views

urlpatterns = patterns('',
url(r'^blog/$', views.blog_list, name='blog_list'),
url(r'^blog/add/$', views.blog_edit, name = 'blog_edit'),
url(r'^blog/del/$', views.blog_del, name = 'blog_del'), )