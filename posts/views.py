import self as self
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .models import Post, Group
from .forms import CreateForm

def authorized_only(func):
    # Функция-обёртка в декораторе может быть названа как угодно
    def check_user(request, *args, **kwargs):
        # В любую view-функцию первым аргументом передаётся объект request,
        # в котором есть булева переменная is_authenticated,
        # определяющая, авторизован ли пользователь.
        if request.user.is_authenticated:
            # Возвращает view-функцию, если пользователь авторизован.
            return func(request, *args, **kwargs)
        # Если пользователь не авторизован — отправим его на страницу логина.
        return redirect('/auth/login/')
    return check_user


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
    post = post_list.first()
    context = {
        'group': group,
        'page_obj': page_obj,
        'post': post,
    }
    return render(request, 'posts/group_list.html', context=context)

def profile(request, username):
    posts = Post.objects.filter(author__username=username).order_by('-pub_date')
    post_count = posts.count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    post = posts.first()
    context = {
        'page_obj': page_obj,
        'count': post_count,
        'post': post,
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

@authorized_only
def post_create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts:index')
    else:
        form = CreateForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context=context)

class PostEdit(UpdateView):
    model = Post
    template_name = 'posts/create.html'
    form_class = CreateForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(PostEdit, self).dispatch(request, *args, **kwargs)

