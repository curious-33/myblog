from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostListView(ListAPIView):
    queryset = Post.objects.all().order_by("-updated_at")
    serializer_class = PostSerializer


class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = 'pk'
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


