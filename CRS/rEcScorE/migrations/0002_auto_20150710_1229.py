# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(null=True, upload_to=b'/rEcScorE/images/', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 10, 12, 29, 15, 663726, tzinfo=utc), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 10, 12, 29, 15, 663818, tzinfo=utc), null=True, blank=True),
        ),
    ]
