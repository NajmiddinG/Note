from django.contrib import admin
from .models import (CheckingTask, Note, Image, Category, Task, MapTask, SubMapTask)

@admin.register(CheckingTask)
class CheckingTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'progress', 'finish_time')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('folder_name', 'user')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','name')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('header', 'category', 'finish_time')


@admin.register(MapTask)
class MapTaskAdmin(admin.ModelAdmin):
    list_display = ('header', 'category', 'progress', 'finish_time')
    

@admin.register(SubMapTask)
class SubMapTaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'progress', 'finish_time')
