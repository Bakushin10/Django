from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Post
from .serializers import UserSerializer, PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(APIView):

    def get(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

        
    def post(self, request):
        # queryset = Post.objects.all()
        # serializer_class = PostSerializer

        serializer_class = PostSerializer(data=request.data)
        if not serializer_class.is_valid():
            print("invalid data")
            print(serializer_class.data)
            return HttpResponse("requested model invalid")
        
        print("valid data")
        serializer_class.save()
        return HttpResponse(serializer_class)


