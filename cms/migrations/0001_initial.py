# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u30bf\u30a4\u30c8\u30eb')),
                ('date', models.CharField(max_length=255, verbose_name='\u6295\u7a3f\u65e5\u6642')),
                ('tag', models.CharField(max_length=255, verbose_name='\u30bf\u30b0')),
                ('log_body', models.TextField(verbose_name='\u672c\u6587', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
