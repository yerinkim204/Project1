from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)    # 책 제목
    author = models.CharField(max_length=50)    # 저자
    publisher = models.CharField(max_length=50) # 출판사
    description = models.TextField()           # 책 소개
    
    def __str__(self):
        return self.title