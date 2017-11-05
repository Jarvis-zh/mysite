#-*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    post_list = Post.objects.all()[:4]
    context = {'post_list' : post_list}
    return render(request, 'myblog/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'myblog/detail.html', context)

def about(request):
    return render(request, 'myblog/about.html')

def contact(request):
    return render(request, 'myblog/contact.html')

def post_list(request):
    post_list = Post.objects.all()
    context = {'post_list' : post_list}
    return render(request, 'myblog/post_list.html', context)