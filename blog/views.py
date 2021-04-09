from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    CreateAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from .permissions import IsAuthorOrReadOnly


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = "post-list"


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = 'pk'
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    name = "post-detail"


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = "create-post"


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = "category-list"


class CategoryView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    name = "category-detail"
