from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ProjectViewSet



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'project', ProjectViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]