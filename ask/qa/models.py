# -*- coding: utf8 -*-
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


class QuestionManager(models.Manager):
    def new(self):
        return super().get_queryset().order_by('-added_at')

    def popular(self):
        return super().get_queryset().order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()

    title = models.CharField(max_length=250)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='like_user')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(to=Question, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
