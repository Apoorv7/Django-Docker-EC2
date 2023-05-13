from django.urls import path, include
from .views import index,Project, Project_by_user

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('project/', Project.as_view(), name='project'),
    path('project/<user>', Project_by_user.as_view(), name='project_by_user'),
]


