from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    # Если порядок сортировки определен в классе Meta модели,
    # запрос будет выглядеть так:
    # post_list = Post.objects.all()
    # Показывать по 10 записей на странице.
    paginator = Paginator(post_list, 10)

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)

    # Отдаем в словаре контекста
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.all().filter(group=group).order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context=context)

def profile(request, username):
    posts = Post.objects.filter(author__username=username).order_by('-pub_date')
    post_count = posts.count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'count': post_count,
    }
    return render(request, 'posts/profile.html', context=context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    posts = Post.objects.filter(author__username=post.author.username).count()
    context = {
        'post': post,
        'posts': posts,
    }
    return render(request, 'posts/post_detail.html', context=context)

def post_create(request):
    pass


