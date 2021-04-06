from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_user_model')

    def get_author(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user

    class Meta:
        model = Post
        exclude = ('date_updated',)

    def create(self, validated_data):
        _Post = Post(
            author=self.context['request'].user
        )
        _Post.save()
        return _Post

