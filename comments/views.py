#-*- coding:utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from myblog.models import Post

from .models import Comment
from .forms import CommentForm

def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            #将评论和文章关联起来
            comment.post = post
            comment.save()

            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {
                'post' : post,
                'form' : form,
                'comment_list' : comment_list
            }

            return render(request, 'myblog/detail.html', context=context)

    #不是POST请求，重定向到文章详情页
    return redirect(post)