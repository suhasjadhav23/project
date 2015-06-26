# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0007_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='NT_skill',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='employee',
            name='T_skill',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(default=b'mycity', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='country',
            field=models.CharField(default=b'mycountry', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(default=b'desgn', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='highest_degree',
            field=models.CharField(default=b'degree', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='your_name',
            field=models.CharField(default=b'name', max_length=100),
        ),
    ]
