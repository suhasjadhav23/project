# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0008_auto_20150626_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='country',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='highest_degree',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='your_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
