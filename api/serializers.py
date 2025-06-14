from rest_framework import serializers
from .models import Blog, Comment, Like

class BlogSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField(many=True, read_only=True)
    likes = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
        extra_kwargs = {
            'author' : { 'read_only':True }
        }

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'author' : { 'read_only':True },
            'blog' : {'read_only':True }
        }

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        extra_kwargs = {
            'author' : { 'read_only':True },
            'blog' : { 'read_only':True }
        }

    def save(self, blog, author):

        if Like.objects.filter(author=author).filter(blog_id=blog).exists():
            raise serializers.ValidationError('This user has already liked this blog')
        self.save(blog_id=blog, author=author)
