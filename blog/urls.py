from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    CategoryListView,
    CategoryView
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name="post-list"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('posts/create/', PostCreateView.as_view(), name="create-post"),
    path('categories/', CategoryListView.as_view(), name="category-list"),
    path('categories/<slug:slug>/', CategoryView.as_view(), name="category-detail")
]