from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticatedOrReadOnly, AllowAny, DjangoModelPermissionsOrAnonReadOnly

from webapp.models import Project, Task
from api.serializers import ProjectSerializer, TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
