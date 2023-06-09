# Generated by Django 3.2.9 on 2023-04-10 10:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20230410_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='checkingtask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 10, 32, 42, 119688, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='maptask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 10, 32, 42, 123911, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='submaptask',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 10, 32, 42, 124749, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 10, 32, 42, 122840, tzinfo=utc)),
        ),
    ]
