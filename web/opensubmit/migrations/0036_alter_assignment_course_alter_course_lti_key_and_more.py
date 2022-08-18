# Generated by Django 4.0.6 on 2022-07-18 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opensubmit', '0035_auto_20181011_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='opensubmit.course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='lti_key',
            field=models.CharField(blank=True, default='da08ee7e06ab11ed86bc8d704d24de30', help_text='Key to be used by an LTI consumer when accessing this course.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='lti_secret',
            field=models.CharField(blank=True, default='da08ee7f06ab11ed86bc8d704d24de30', help_text='Secret to be used by an LTI consumer when accessing this course.', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='opensubmit.assignment'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submitted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='submissiontestresult',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to='opensubmit.testmachine'),
        ),
        migrations.AlterField(
            model_name='submissiontestresult',
            name='submission_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to='opensubmit.submissionfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='courses',
            field=models.ManyToManyField(blank=True, limit_choices_to={'active__exact': True}, related_name='participants', to='opensubmit.course'),
        ),
    ]
