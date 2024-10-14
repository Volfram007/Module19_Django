from django.db import models


class Buyer(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField('Логин', max_length=200)  # Логин пользователя
    password = models.CharField('Пароль', max_length=200, default='')  # Пароль пользователя
    balance = models.DecimalField('Баланс', max_digits=10, decimal_places=2, default=110.00)
    age = models.IntegerField('Возраст', default=100)  # Возраст пользователя

    def __str__(self):
        return self.name


class Game(models.Model):
    objects = None
    title = models.CharField('Игра', max_length=200)  # Название игры
    cost = models.DecimalField('Цена', max_digits=8, decimal_places=2)  # Стоимость игры
    size = models.DecimalField('Размер', max_digits=6, decimal_places=2)  # Размер игры
    description = models.TextField('Описание', )  # Описание игры
    age_limited = models.BooleanField('Ограничение', default=False)  # Ограничение по возрасту 18+
    buyer = models.ManyToManyField(Buyer)  # Кто купил игру

    def __str__(self):
        return self.title
