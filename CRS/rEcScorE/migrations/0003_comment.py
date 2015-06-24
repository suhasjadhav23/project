# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0002_icecream'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('second_name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
