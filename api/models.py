from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.author.username + " | " + self.comment

class Like(models.Model):
    like = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        if self.like :
            return self.author.username + "| Like"
        return self.author.username + " | Unlike"

    class Meta:
        unique_together = ('author', 'blog')
