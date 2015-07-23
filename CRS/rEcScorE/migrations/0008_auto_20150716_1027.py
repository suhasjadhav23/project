# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rEcScorE', '0007_auto_20150716_0549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='second_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 10, 27, 39, 338269, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 10, 27, 39, 338358, tzinfo=utc), null=True, blank=True),
        ),
    ]
