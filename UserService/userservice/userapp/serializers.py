from django.contrib.auth.models import User
from rest_framework import serializers
from django.core import exceptions
import django.contrib.auth.password_validation as validators
from .models import Project


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','id', 'username', 'email', 'is_staff', 'password']
        
        extra_kwargs = {
            'url':{'lookup_field':'username'},
        }

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        