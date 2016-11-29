# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_useraccount_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='birthday',
            field=models.CharField(default='x', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='password',
            field=models.BinaryField(max_length=512),
        ),
    ]