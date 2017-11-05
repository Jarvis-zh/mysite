#-*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag

def index(request):
    post_list = Post.objects.all()[:4]
    context = {'post_list' : post_list}
    return render(request, 'myblog/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    #粗略统计阅读量
    post.views += 1

    context = {'post': post}
    return render(request, 'myblog/detail.html', context)

def about(request):
    return render(request, 'myblog/about.html')

def contact(request):
    return render(request, 'myblog/contact.html')

def all_post(request):
    post_list = Post.objects.all()
    context = {'post_list' : post_list}
    return render(request, 'myblog/post_list.html', context)

#归档页面
def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by('-created_time')
    return render(request, 'myblog/post_list.html', {'post_list' : post_list})

#分类页面
def category(request, pk):
    temp_category = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=temp_category).order_by('-created_time')
    return render(request, 'myblog/post_list.html', {'post_list': post_list})

#标签云页面
def tags(request, pk):
    temp_tag = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=temp_tag).order_by('-created_time')
    return render(request, 'myblog/post_list.html', {'post_list': post_list})
