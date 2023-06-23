# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-06-22 12:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSubscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_time', models.DateTimeField(default=datetime.datetime.now)),
                ('opened', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='emailcampaign',
            name='celery_task_id',
            field=models.CharField(default=b'', max_length=36),
        ),
        migrations.AddField(
            model_name='emailsubscriber',
            name='campaign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sender.EmailCampaign'),
        ),
        migrations.AddField(
            model_name='emailsubscriber',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sender.Subscriber'),
        ),
    ]