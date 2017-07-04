# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-02 00:30
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20170702_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyactivity',
            name='base_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='dailyactivity',
            name='timestamp',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=[], null=True),
        ),
        migrations.AlterField(
            model_name='dailyactivity',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
