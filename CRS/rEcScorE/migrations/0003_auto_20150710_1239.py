# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0002_auto_20150710_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='image',
            new_name='Profile_Pic',
        ),
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 10, 12, 39, 32, 883975, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 10, 12, 39, 32, 884112, tzinfo=utc), null=True, blank=True),
        ),
    ]
