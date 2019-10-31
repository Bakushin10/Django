from django.shortcuts import render
from rest_framework import viewsets, status
from .models import User, Post
from .serializers import UserSerializer, PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
import requests

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(APIView):

    def post(self, request, **kwargs):
        base_URL = request._request._current_scheme_host
        weatherLocation = kwargs.get("location", None)
        print("{} {}".format("weatherLocation", weatherLocation))
        if weatherLocation:
            weatherAPITemplate = base_URL + "/weather/{}/"
            print(weatherAPITemplate.format(weatherLocation))
            city_weather = requests.post(weatherAPITemplate.format(weatherLocation), params=request.POST)
            return Response(data = city_weather, status = status.HTTP_200_OK)

        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(data = serializer.data, status = status.HTTP_400_BAD_REQUEST)

        
    # def post(self, request, **kwargs):
    #     # queryset = Post.objects.all()
    #     # serializer_class = PostSerializer

    #     serializer_class = PostSerializer(data=request.data)
    #     print(serializer_class)
    #     if not serializer_class.is_valid():
    #         print("invalid data")
    #         print(serializer_class.data)
    #         return HttpResponse("requested model invalid")
        
    #     print("valid data")
    #     print(serializer_class.data)
    #     #serializer_class.save()
    #     return HttpResponse(serializer_class)


