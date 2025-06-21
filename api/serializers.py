from rest_framework import serializers
from .models import Blog, Comment, Like
from django.contrib.auth.models import User

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


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']
        extra_kwargs = {
            'password': { 'write_only':True }
        }

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('This username already exists, pick a unique username')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('This email already used, use a different email')

        if password!=password_confirm:
            raise serializers.ValidationError("Passwords don't match")

        account = User(username=username, email=email)
        account.set_password(password)
        account.save()

        return account
