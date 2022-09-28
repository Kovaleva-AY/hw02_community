from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Post, Group, User

POSTS_NUMBER = 10


def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    paginator = Paginator(group.posts.all(), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    posts = group.posts.all()[:10]
    context = {
        'group': group,
        'paginator': paginator,
        'page_number': page_number,
        'page_obj': page_obj,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Post.objects.all()
    paginator = Paginator(author.posts.all(), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    post_count = posts.count()
    context = {
        'author': author,
        'paginator': paginator,
        'page_number': page_number,
        'page_obj': page_obj,
        'posts': posts,
        'post_count': post_count
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    posts = get_object_or_404(Post, pk=post_id)
    context = {
        'posts': posts,

    }
    return render(request, 'posts/post_detail.html', context) 
    