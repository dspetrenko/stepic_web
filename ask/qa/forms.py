# -*- coding: utf8 -*-

from django.forms import ModelForm
from django.forms import Form

from django.forms.widgets import TextInput
from django.forms.widgets import PasswordInput


from .models import Question, Answer


class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'text',
        ]


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = [
            'question',
            'text',
        ]


class Signupform(Form):

    username = TextInput()
    email = TextInput()
    password = PasswordInput()
