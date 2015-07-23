# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0006_auto_20150716_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 5, 49, 24, 478235, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 5, 49, 24, 478337, tzinfo=utc), null=True, blank=True),
        ),
    ]
