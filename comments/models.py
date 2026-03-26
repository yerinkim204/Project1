from django.db import models
from blog.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # blog 앱의 Post와 연결
    author = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
