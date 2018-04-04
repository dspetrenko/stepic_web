from django.shortcuts import render

from django.http import HttpResponse

from django.core.paginator import Paginator

from .models import Question as Q


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main(request):
    page_number = request.GET.get('page', 1)

    qul = Q.objects.new()

    limit = 10
    paginator = Paginator(qul, limit)
    questions_list = paginator.get_page(page_number)

    context = {
        'questions_list': questions_list,
    }
    return render(request, 'questions.html', context=context)


def popular(request):
    page = request.GET.get('page')

    return HttpResponse('OK\tpage={}'.format(page))


def question(request, id):
    return HttpResponse('OK')
