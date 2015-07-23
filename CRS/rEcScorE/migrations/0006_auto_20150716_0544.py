# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0005_auto_20150716_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Profile_Pic',
            field=models.ImageField(null=True, upload_to=b'img/documents/', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 5, 44, 46, 996827, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 5, 44, 46, 996923, tzinfo=utc), null=True, blank=True),
        ),
    ]
