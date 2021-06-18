from rest_framework import generics
from backend.apps.blog.models import Post
from .serializers import PostSerializer


class PostsListView(generics.ListCreateAPIView):
    queryset = Post.published_posts_objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
