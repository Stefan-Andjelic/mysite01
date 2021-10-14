from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.publish.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, day, month, year, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})