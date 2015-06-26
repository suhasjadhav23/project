# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rEcScorE', '0011_employee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='NT_skill',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='T_skill',
        ),
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateField(null=True, verbose_name=b'Date Of Birth ', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='doj',
            field=models.DateField(null=True, verbose_name=b'Date Of Joining ', blank=True),
        ),
    ]
