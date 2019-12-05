from rest_framework import serializers

from webapp.models import Project, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'summary', 'description', 'status', 'type', 'project', 'assigned_to')


class ProjectSerializer(serializers.ModelSerializer):
    projects = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'users', 'projects')
