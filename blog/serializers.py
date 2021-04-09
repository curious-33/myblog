from rest_framework import serializers
from .models import Post, Category
from django.contrib.auth import get_user_model


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='user-info')
    posts = serializers.HyperlinkedRelatedField(many=True, view_name="post-detail", read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts']


# class TagSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = Tag
#         fields = ('url', 'title')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('created_at', 'author', 'published_at', 'views')



