# Generated by Django 3.2.9 on 2023-04-10 09:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20230410_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkingtask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 9, 19, 5, 421916, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='checkingtask',
            name='repeat',
            field=models.CharField(choices=[('1', 'Never'), ('2', 'Every day'), ('3', 'Monday to Friday'), ('4', 'Every week'), ('5', 'Every month'), ('6', 'Every year')], max_length=1),
        ),
        migrations.AlterField(
            model_name='maptask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 9, 19, 5, 426541, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='submaptask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 9, 19, 5, 427388, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 9, 19, 5, 425502, tzinfo=utc)),
        ),
    ]
