# Generated by Django 5.1.1 on 2024-10-11 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task3', '0002_alter_buyer_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='password',
            field=models.CharField(default='', max_length=200, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='age',
            field=models.IntegerField(default=100, verbose_name='Возраст'),
        ),
    ]