#coding:utf-8
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(u'タイトル',max_length=255)
    date = models.CharField(u'投稿日時',max_length=255)
    tag = models.CharField(u'タグ',max_length=255)
    log_body = models.TextField(u'本文',blank=True)

    def __unicode__(self):
        return self.title