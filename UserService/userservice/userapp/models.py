from django.db import models
from django.conf import settings


class Project(models.Model):
    project_choice=(
        ('Engineering','Engineering'),
        ('Support','Support'),
        ('HR','HR')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    project_type = models.CharField(max_length=20,choices=project_choice,null=False)
    added_timestamp = models.DateTimeField('%Y-%m-%d %H:%M:%S',auto_now_add=True)

