from rest_framework import routers

from .viewsets import UserViewSet

app_name = "users"

routers = routers.DefaultRouter()
routers.register('users',UserViewSet)