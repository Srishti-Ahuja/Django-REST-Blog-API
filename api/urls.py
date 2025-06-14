from django.urls import path, include
from .views import BlogList, BlogDetail, CommentList, CommentDetail, LikeList, LikeDetail

urlpatterns = [
    path('blog/', BlogList.as_view(), name='blog-list'),
    path('blog/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('blog/<int:pk>/comments/', CommentList.as_view(), name='comment-list'),
    path('blog/comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('blog/<int:pk>/like/', LikeList.as_view(), name='like-list'),
    path('blog/like/<int:pk>/', LikeDetail.as_view(), name='like-detail')
]
