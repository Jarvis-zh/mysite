#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    """
    Category : 文章的分类归档，每篇文章只能有一种分类归档
    """
    # 分类名称
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    Tag : 文章的标签，每篇文章可能有多个标签
    """
    # 标签名称
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    Post : 文章主体
    """
    # 标题
    title = models.CharField(max_length=100)
    # 内容
    body = models.TextField()
    # 创建时间
    created_time = models.DateTimeField()
    # 修改时间
    modified_time = models.DateTimeField()
    # 文章摘要 ，可以为空
    excerpt = models.CharField(max_length=100)
    # 文章作者
    author = models.ForeignKey(User)
    # 文章分类
    category = models.ForeignKey(Category)
    # 文章标签, 允许为空
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title