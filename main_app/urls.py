from django.urls import path, include
from rest_framework import routers

from .views import (CheckingTaskViewSet, NoteViewSet, ImageViewSet, CategoryViewSet, TaskViewSet, MapTaskViewSet, SubMapTaskViewSet)

router = routers.DefaultRouter()
router.register(r'checking-task', CheckingTaskViewSet)
router.register(r'note', NoteViewSet)
router.register(r'image', ImageViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'task', TaskViewSet)
router.register(r'map-task', MapTaskViewSet)
router.register(r'sub-map-task', SubMapTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
