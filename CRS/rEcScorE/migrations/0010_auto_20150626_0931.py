# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0009_auto_20150626_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default=datetime.date(2015, 6, 26), verbose_name=b'Date Of Birth '),
        ),
        migrations.AddField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default=datetime.date(2015, 6, 26), verbose_name=b'Date Of Joining '),
        ),
    ]
