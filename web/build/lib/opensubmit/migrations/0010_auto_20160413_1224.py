# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-13 12:24


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensubmit', '0009_auto_20151127_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lti_key',
            field=models.CharField(help_text=b'Key to be used by an LTI consumer when accessing this course.', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='lti_secret',
            field=models.CharField(help_text=b'Secret to be used by an LTI consumer when accessing this course.', max_length=100, null=True),
        ),
    ]
