from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, ProjectSerializer
from django.contrib.auth.models import User
from .models import Project


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
