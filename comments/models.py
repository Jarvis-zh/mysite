#-*- coding:utf-8 -*-

from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(max_length=255, blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True) #自动将当前时间指定为评论时间

    post = models.ForeignKey('myblog.Post')

    def __str__(self):
        return self.text[:20]

