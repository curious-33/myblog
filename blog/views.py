from rest_framework.generics import (
        ListAPIView,
        RetrieveAPIView,
    )
from .models import Post
from .serializers import PostSerializer


class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    lookup_field = 'pk'
    serializer_class = PostSerializer
