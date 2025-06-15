from django.shortcuts import render
from .models import Blog, Comment, Like
from .serializers import BlogSerializer, CommentSerializer, LikeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.throttling import UserRateThrottle
from .throttling import BlogPostThrottle
from .pagination import BlogPagination, CommentPagination

# Create your views here.
class BlogList(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    throttle_classes = (BlogPostThrottle, )
    pagination_class = BlogPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class CommentList(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    throttle_classes = (UserRateThrottle, )
    pagination_class = CommentPagination

    def get_queryset(self):
        return Comment.objects.filter(blog_id=self.kwargs['pk'])

    def perform_create(self, serializer):
        blog = Blog.objects.get(pk=self.kwargs['pk'])
        serializer.save(author=self.request.user, blog=blog)

class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class LikeList(ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Like.objects.filter(blog_id=self.kwargs['pk'])

    def perform_create(self, serializer):
        serializer.save(blog=self.kwargs['pk'], author=self.request.user)

class LikeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = (IsOwnerOrReadOnly,)
