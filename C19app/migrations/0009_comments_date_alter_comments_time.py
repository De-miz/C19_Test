# Generated by Django 4.1.2 on 2022-10-27 22:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('C19app', '0008_remove_comments_date_alter_comments_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 27, 0, 0)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
