#coding:utf-8
from django.contrib import admin
from cms.models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','date','tag','log_body')
    list_display_links = ('id','title',)

admin.site.register(Blog, BlogAdmin)

