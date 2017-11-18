#-*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag


#首页
class IndexView(ListView):
    model = Post
    template_name = 'myblog/index.html'
    context_object_name = 'post_list'

#归档页面
class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month)
#分类
class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)
#标签
class TagsView(IndexView):
    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagsView, self).get_queryset().filter(tags=tag)

#文章全文
class PostDetailView(DetailView):
    model = Post
    template_name = 'myblog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(self, request, *args, **kwargs)
        self.object.increase_views() #每次获取简单计数，认为阅读量加一
        return response


def about(request):
    return render(request, 'myblog/about.html')

def contact(request):
    return render(request, 'myblog/contact.html')