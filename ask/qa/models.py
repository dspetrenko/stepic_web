from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
4) В вашем приложении qa  в файле models.py определите следующие модели обладающие следующими полями (названия моделей и полей важны!)

Question - вопрос
title - заголовок вопроса
text - полный текст вопроса
added_at - дата добавления вопроса
rating - рейтинг вопроса (число)
author - автор вопроса
likes - список пользователей, поставивших "лайк"

Answer - ответ
text - текст ответа
added_at - дата добавления ответа
question - вопрос, к которому относится ответ
author - автор ответа

В качестве модели пользователя - используйте django.contrib.auth.models.User  из стандартной системы авторизации Django.

5) Рядом с моделью Question определите менеджер реализующий следующие методы

QuestionManager - менеджер модели Question
new - метод возвращающий последние добавленные вопросы
popular - метод возвращающий вопросы отсортированные по рейтингу
"""


class Question(models.Model):

    title = models.CharField()
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User)
