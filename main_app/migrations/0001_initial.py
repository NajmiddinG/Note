# Generated by Django 3.2.9 on 2023-04-10 08:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='MapTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255)),
                ('type', models.BooleanField(default=True)),
                ('progress', models.BooleanField(default=True)),
                ('finish_time', models.DateTimeField(default=datetime.datetime(2023, 4, 11, 8, 31, 16, 424788, tzinfo=utc))),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=1000)),
                ('type', models.BooleanField(default=True)),
                ('finish_time', models.DateTimeField(default=datetime.datetime(2023, 4, 11, 8, 31, 16, 423509, tzinfo=utc))),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.category')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.image')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.note')),
            ],
        ),
        migrations.CreateModel(
            name='SubMapTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('progress', models.BooleanField(default=True)),
                ('finish_time', models.DateTimeField(default=datetime.datetime(2023, 4, 11, 8, 31, 16, 429177, tzinfo=utc))),
                ('connected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submaptask', to='main_app.maptask')),
                ('parent_subtask', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_subtask', to='main_app.submaptask')),
            ],
        ),
        migrations.AddField(
            model_name='maptask',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.note'),
        ),
        migrations.CreateModel(
            name='CheckingTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('finish_time', models.DateTimeField(default=datetime.datetime(2023, 4, 11, 8, 31, 16, 419946, tzinfo=utc))),
                ('progress', models.BooleanField(default=True)),
                ('repeat', models.CharField(choices=[(1, 'Never'), (2, 'Every day'), (3, 'Monday to Friday'), (4, 'Every week'), (5, 'Every month'), (6, 'Every year')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]