from rest_framework import serializers
from .models import User, Post, NumList

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name',)
        extra_kwargs = { 'id': { 'read_only': False } }


class NumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumList
        fields = ('id', 'num1', 'num2', "num3")
        extra_kwargs = { 'id': { 'read_only': False } }




class PostSerializer(serializers.ModelSerializer):
    # author is now UserSerializer object
    author = UserSerializer()
    nums = NumListSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author', 'nums', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
    
    
    def create(self, validated_data):
        print(validated_data)
        user_data = validated_data.pop('author')
        nums_data = validated_data.pop('nums')

        # create an user object to set author
        user = User.objects.create(name=dict(user_data)["name"])
        nums = NumList.objects.create(num1=dict(nums_data)["num1"], num2=dict(nums_data)["num2"])
        post = Post.objects.create(author=user, nums=nums, **validated_data)
        return post
    # {
    #     "title": "555",
    #     "body": "this is body 2asdf",
    #     "author": {
    #         "id": 13,
    #         "name": "shin"
    #     },
    #     "nums": {
    #     	"id": 13,
    #         "num1": "13",
    #         "num2": "1ss5"
    #     }
    #  }