# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_enrollment_classsec'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='birthday',
            field=models.DateField(default='x', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='city',
            field=models.CharField(default='x', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useraccount',
            name='profileText',
            field=models.CharField(default='x', max_length=1000),
            preserve_default=False,
        ),
    ]