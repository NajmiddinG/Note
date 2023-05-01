from rest_framework import serializers
from .models import (CheckingTask, Note, Image, Category, Task, MapTask, SubMapTask)


class CheckingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckingTask
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class MapTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapTask
        fields = '__all__'


class SubMapTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMapTask
        fields = '__all__'
