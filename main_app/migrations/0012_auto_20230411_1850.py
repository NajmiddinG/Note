# Generated by Django 3.2.9 on 2023-04-11 18:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20230411_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkingtask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 12, 18, 50, 16, 789975, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maptask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 12, 18, 50, 16, 793060, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='submaptask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 12, 18, 50, 16, 793784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 12, 18, 50, 16, 792403, tzinfo=utc)),
        ),
    ]
