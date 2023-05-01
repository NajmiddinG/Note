# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import (CheckingTask, Note, Image, Category, Task, MapTask, SubMapTask)
from .serializers import (CheckingTaskSerializer, NoteSerializer, ImageSerializer, CategorySerializer, TaskSerializer, MapTaskSerializer, SubMapTaskSerializer)


class CheckingTaskViewSet(ModelViewSet):
    queryset = CheckingTask.objects.all()
    serializer_class = CheckingTaskSerializer


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class MapTaskViewSet(ModelViewSet):
    queryset = MapTask.objects.all()
    serializer_class = MapTaskSerializer


class SubMapTaskViewSet(ModelViewSet):
    queryset = SubMapTask.objects.all()
    serializer_class = SubMapTaskSerializer
