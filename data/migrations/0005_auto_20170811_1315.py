# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-11 13:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_desktop_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailyactivity',
            options={'verbose_name': 'Daily Activity', 'verbose_name_plural': 'Daily Activities'},
        ),
    ]