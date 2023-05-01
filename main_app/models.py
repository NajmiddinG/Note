from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


repeat = [
    ('1', "Never"),
    ('2', "Every day"),
    ('3', "Monday to Friday"),
    ('4', "Every week"),
    ('5', "Every month"),
    ('6', "Every year"),
]


class CheckingTask(models.Model):
    """
    This is a task class that can be check for a period of time of permenantly.
    """
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    finish_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=1))
    progress = models.BooleanField(default=True)
    repeat = models.CharField(choices=repeat, max_length=1)

    def __str__(self):
        return f"{self.user.username} - {self.name}"

    class Meta:
        verbose_name = 'Checking task'
        verbose_name_plural = '1. Checking tasks'


class Note(models.Model):
    """
    This is a task class that can be mapping and default notes for a period of time of permenantly.
    """
    folder_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.folder_name

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = '2. Notes'


class Image(models.Model):
    """
    This is image class for store images to use as a backround for content tasks.
    """
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Background images'
        verbose_name_plural = '3. Background images for a note'


class Category(models.Model):
    """
    This is category class for users to be able to create their own categories for tasks.
    """
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = '4. Categories for notes'


class Task(models.Model):
    """
    This is a task class for writing content.
    """
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    type = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    finish_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=1))
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header
    
    class Meta:
        verbose_name = 'Content task'
        verbose_name_plural = '5. Content tasks'


class MapTask(models.Model):
    """
    This is map task class which is very usefull if you have a lot of tasks and all of them need to be connected to each others.
    """
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    type = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    progress = models.BooleanField(default=True)
    finish_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=1))
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header
    
    class Meta:
        verbose_name = 'Map task'
        verbose_name_plural = '6. Map tasks'


class SubMapTask(models.Model):
    """
    This is sub map task class which is connected to map task class as an child or as an it's child.
    """
    connected = models.ForeignKey(MapTask, on_delete=models.CASCADE, related_name='submaptask')
    parent_subtask = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child_subtask')
    name = models.CharField(max_length=255)
    progress = models.BooleanField(default=True)
    finish_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=1))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sub map task'
        verbose_name_plural = '7. Sub map tasks'
