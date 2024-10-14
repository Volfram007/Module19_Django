from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from datetime import date
from task4.models import *

'''Задание 5'''


def news(request):
    posts = GameNews.objects.all()
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'TitlePage': 'Новости GameNews',
        'username': request.session.get('username'),
        'page_obj': page_obj,
    }
    return render(request, 'task4/news.html', context)


'''Задание 4'''


def task4db(request):
    GameNews.objects.all().delete()
    GameNews.objects.create(
        title="Первая статья",
        content="Содержание первой статьи",
        author="admin",
        published_date=date(2024, 10, 8),
    )
    GameNews.objects.create(
        title="Вторая статья",
        content="Содержание второй статьи",
        author="user1",
        published_date=date(2023, 5, 10),
    )
    GameNews.objects.create(
        title="Третья статья",
        content="Содержание третьей статьи",
        author="user2",
        published_date=date.today(),
    )
    GameNews.objects.create(
        title="Пятая статья",
        content="Содержание пятой статьи",
        author="admin",
        published_date=date.today(),
    )

    return redirect('news')  # Перенаправление на страницу авторизации
