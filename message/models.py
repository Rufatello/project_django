from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    email = models.EmailField(verbose_name='Почта', max_length=250)
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    surname = models.CharField(max_length=100, verbose_name='Отчество')
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return f'{self.first_name} {self.last_name}{self.surname},{self.email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    title = models.CharField(verbose_name='Тема письма', max_length=250)
    body_message = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return f'{self.title}{self.body_message}'

    class Meta:
        verbose_name = 'Пиьсмо'
        verbose_name_plural = 'Письма'





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user_image/', verbose_name='Аватар')

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'