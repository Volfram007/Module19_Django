from django.shortcuts import render, redirect
from task3.models import *
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    return render(request, 'index.html')


'''Задание 3'''


def authorization(request):
    context = {
        'TitlePage': 'Авторизация',
    }
    if request.session.get('user_id'):  # Если пользователь уже авторизован
        return redirect('main')
    if request.method == 'POST':
        # data = request.POST
        # print(data)

        info = {}
        form_type = request.POST.get('tab_act')

        if form_type == 'login':
            # Обработка формы входа
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Логика аутентификации пользователя
            try:
                # user = Buyer.objects.get(name=username)
                user = Buyer.objects.get(name__iexact=username.lower())
                # Проверка пароля
                # if check_password(password, user.password):
                if password == user.password:
                    # Сохранение информации о пользователе в сессии
                    request.session['user_id'] = user.id
                    request.session['username'] = user.name
                    return redirect('main')
                else:
                    context['error'] = 'Неверный пароль.'
            except Buyer.DoesNotExist:
                context['error'] = 'Пользователь не найден.'
            return render(request, 'task3/authorization.html', context)
        elif form_type == 'register':
            # Обработка формы регистрации
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')
            # Проверка паролей и создание нового пользователя
            if password != repeat_password:
                context['error'] = 'Пароли не совпадают'
            elif len(password or repeat_password) < 0:
                context['error'] = 'Длина пароля должна быть не менее 8-х символов'
            # elif int(age) < 18:
            #     context['error'] = 'Вы должны быть старше 18'
            elif not age:
                context['error'] = 'Введите возраст'
            else:
                # Создание пользователя
                user_exists = Buyer.objects.filter(name=username).exists()
                if not user_exists:
                    # hashed_password = make_password(password)
                    user = Buyer.objects.create(name=username, password=password, age=age)
                    # Сохранение информации о пользователе в сессии
                    request.session['user_id'] = user.id
                    request.session['username'] = user.name
                    return redirect('main')
                else:
                    context['error'] = 'Пользователь с таким именем уже существует.'
        context['tab_act'] = 'register'
        return render(request, 'task3/authorization.html', context)
    else:
        return render(request, 'task3/authorization.html', context)


def logout(request):
    # Очистка всех данных сессии
    request.session.flush()
    return redirect('authorization')  # Перенаправление на страницу авторизации


def main(request):
    context = {
        'TitlePage': 'Главная',
        'username': request.session.get('username'),
    }
    return render(request, 'task3/main.html', context)


def shop(request):
    games = Game.objects.all
    context = {
        'TitlePage': 'Магазин',
        'username': request.session.get('username'),
        'games': games,
    }
    return render(request, 'task3/shop.html', context)


def cart(request):
    games = Game.objects.filter(buyer__id=request.session.get('user_id'))
    context = {
        'TitlePage': 'Корзина',
        'username': request.session.get('username'),
        'games': games,
    }
    return render(request, 'task3/cart.html', context)


def task3db(request):
    Buyer.objects.all().delete()
    Game.objects.all().delete()
    buyer1 = Buyer.objects.create(name="User1", balance=100.00, age=20)
    buyer2 = Buyer.objects.create(name="User2", balance=150.00, age=24)
    buyer3 = Buyer.objects.create(name="User3", balance=100.00, age=15)
    game1 = Game.objects.create(title="Game A", cost=30.00, size=5.00, description="Описание A", age_limited=True)
    game2 = Game.objects.create(title="Game B", cost=40.00, size=10.00, description="Описание B", age_limited=True)
    game3 = Game.objects.create(title="Game C", cost=20.00, size=2.00, description="Описание C", age_limited=False)
    Game.objects.get(title=game1.title).buyer.set((buyer1, buyer2,))
    Game.objects.get(title=game2.title).buyer.set((buyer1, buyer2,))
    Game.objects.get(title=game3.title).buyer.set((buyer1, buyer3,))
    return redirect('authorization')  # Перенаправление на страницу авторизации



