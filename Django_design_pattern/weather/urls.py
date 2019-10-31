from rest_framework import routers
from weather.views import WeatherViewSet 
from django.urls import path

urlpatterns = [
    path("", WeatherViewSet.as_view())
]