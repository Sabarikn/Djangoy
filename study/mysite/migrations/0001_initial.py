# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]
    

    operations = [
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name' ,models.CharField(max_length=120,blank=False)),
                ('marks',models.IntegerField(blank=False)),
                ('userid',models.CharField(max_length=120,blank=False)),
            ],
        ),
    ]
