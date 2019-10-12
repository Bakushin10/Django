from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name',)
        extra_kwargs = { 'id': { 'read_only': False } }

class PostSerializer(serializers.ModelSerializer):
    # author is now UserSerializer object
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
    
    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop('author')
        print(dict(user_data)["name"])
        # create an user object to set author
        user = User.objects.create(name=dict(user_data)["name"])
        post = Post.objects.create(author=user, **validated_data)
        return post
        # {
        #     "id": 2,
        #     "title": "hi",
        #     "body": "this is body 2",
        #     "author": {
        #         "id" : 5,
        #         "name": "my name is.."
        #     }
        # }