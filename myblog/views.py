#-*- coding:utf-8 -*-
from django.shortcuts import render


def index(request):
    return render(request, 'myblog/index.html', None)

def about(request):
    return render(request, 'myblog/about.html', None)

def contact(request):
    return render(request, 'myblog/contact.html', None)

def detail(request):
    return render(request, 'myblog/detail.html', None)
