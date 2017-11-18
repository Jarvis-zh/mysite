#-*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag

def index(request):
    post_list = Post.objects.all()
    page_title = '首页'
    context = {'post_list' : post_list,
               'page_title' : page_title}
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

#归档页面
def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month).order_by('-created_time')
    page_title = '{}年{}月文章'.format(year, month)
    context = {
        'post_list' : post_list,
        'page_title' : page_title
    }
    return render(request, 'myblog/index.html', context)

#分类页面
def category(request, pk):
    temp_category = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=temp_category).order_by('-created_time')
    page_title = '{}类文章'.format(temp_category)
    context = {
        'post_list' : post_list,
        'page_title' : page_title
    }
    return render(request, 'myblog/index.html', context)

#标签云页面
def tags(request, pk):
    temp_tag = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=temp_tag).order_by('-created_time')
    page_title = '{}标签文章'.format(temp_tag)
    context = {
        'post_list' : post_list,
        'page_title' : page_title
    }
    return render(request, 'myblog/index.html', context)
