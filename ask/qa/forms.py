# -*- coding: utf8 -*-

from django.forms import ModelForm


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
