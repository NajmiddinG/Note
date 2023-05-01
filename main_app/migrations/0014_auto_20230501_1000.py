# Generated by Django 3.2.9 on 2023-05-01 10:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20230412_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkingtask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 10, 0, 34, 790523, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='maptask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 10, 0, 34, 793233, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='submaptask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 10, 0, 34, 793896, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 10, 0, 34, 792697, tzinfo=utc)),
        ),
    ]