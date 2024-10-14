"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from task3.views import *
from task4.views import *

urlpatterns = [
    path('', index, name='index'),
    # Task1 реализовать собственные ORM модели и научиться мигрировать их в базу данных (task1\models.py)
    # Task2 сделать первые записи в БД при помощи QuerySet запросов. Файл "Django Shell.txt" в корне проекта
    # Task3 объединение: реализовать БД и взаимодействие с ней через DTL
    path('auth/', authorization, name='authorization'),
    path('main/', main, name='main'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('logout/', logout, name='logout'),
    # Автозаполнение БД
    path('task3db/', task3db, name='task3db'),
    # Task4 администрирование+ Task5 пагинация. Дополнение моделью GameNews (task4\models.py)
    path('admin/', admin.site.urls),
    path('news/', news, name='news'),
    # Автозаполнение БД
    path('task4db/', task4db, name='task4db'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
