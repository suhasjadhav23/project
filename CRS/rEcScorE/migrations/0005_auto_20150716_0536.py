# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0004_auto_20150710_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Profile_Pic',
            field=models.ImageField(null=True, upload_to=b'rEcScore/images/', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 5, 36, 10, 360171, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 5, 36, 10, 360272, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2015, 7, 16)),
        ),
    ]
