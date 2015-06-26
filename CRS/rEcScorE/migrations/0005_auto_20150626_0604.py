# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0004_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=3, choices=[(b'MR', b'Mr.'), (b'MRS', b'Mrs.'), (b'MS', b'Ms.')])),
                ('birth_date', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('authors', models.ManyToManyField(to='rEcScorE.Author')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 6, 26)),
        ),
    ]
