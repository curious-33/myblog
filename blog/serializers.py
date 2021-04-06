from rest_framework import serializers
from .models import Post
from user.serializers import UserInfoSerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserInfoSerializer(read_only=True)
    class Meta:
        model = Post
        exclude = ('date_updated',)
        read_only = ('date_created',)