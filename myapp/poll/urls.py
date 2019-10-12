from rest_framework import routers
from poll.views import UserViewSet, PostViewSet
from django.urls import path

urlpatterns = [
    path("", PostViewSet.as_view())
]
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'posts', PostViewSet)