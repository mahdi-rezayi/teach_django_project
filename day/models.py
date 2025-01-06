from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    post = models.ManyToManyField(Post, related_name='category_post')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    title = models.CharField(max_length=100)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')

    class Meta:
        db_table = 'tbl name'
