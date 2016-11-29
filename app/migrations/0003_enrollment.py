# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161127_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userAccount')),
            ],
        ),
    ]