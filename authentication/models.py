from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''Создание модели Пользователя'''
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'




