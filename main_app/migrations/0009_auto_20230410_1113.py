# Generated by Django 3.2.9 on 2023-04-10 11:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20230410_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkingtask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 11, 13, 35, 396217, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maptask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 11, 13, 35, 400804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='submaptask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 11, 13, 35, 401691, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 11, 13, 35, 399814, tzinfo=utc)),
        ),
    ]
