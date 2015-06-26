# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0012_auto_20150626_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(null=True, verbose_name=b'Date Of Birth ', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(null=True, verbose_name=b'Date Of Joining ', blank=True),
        ),
    ]
