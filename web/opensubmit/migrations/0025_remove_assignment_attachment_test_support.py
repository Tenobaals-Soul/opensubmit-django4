# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-14 14:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensubmit', '0024_auto_20171028_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='attachment_test_support',
        ),
    ]
