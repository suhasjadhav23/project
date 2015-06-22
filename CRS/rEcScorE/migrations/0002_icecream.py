# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flavor', models.CharField(max_length=50)),
                ('status', models.IntegerField(choices=[(0, b'solid'), (1, b'squishy'), (2, b'liquid')])),
            ],
        ),
    ]
