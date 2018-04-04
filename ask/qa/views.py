from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from django.core.paginator import Paginator

from .models import Question as Q
from .models import Answer as A


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main(request):
    page_number = int(request.GET.get('page', 1))

    qul = Q.objects.new()

    limit = 10
    paginator = Paginator(qul, limit)
    questions_list = paginator.get_page(page_number)

    context = {
        'questions_list': questions_list,
    }
    return render(request, 'questions.html', context=context)


def popular(request):
    page_number = int(request.GET.get('page', 1))

    limit = 10
    paginator = Paginator(Q.objects.popular(), limit)
    questions_list = paginator.get_page(page_number)

    context = {
        'questions_list': questions_list,
    }
    return render(request, 'questions.html', context=context)


def question(request, question_id):

    q = get_object_or_404(Q, id=int(question_id))
    context = {
        'question': q,
        'answers': A.objects.filter(question=q)
    }
    return render(request, 'question.html', context=context)
