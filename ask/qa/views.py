from django.shortcuts import render

from django.http import HttpResponse


from .models import Question as Q


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main(request):
    page = request.GET.get('page')

    qul = Q.objects.new()

    context = {
        'questions_list': qul,
    }
    return render(request, 'questions.html', context=context)


def popular(request):
    page = request.GET.get('page')

    return HttpResponse('OK\tpage={}'.format(page))


def question(request, id):
    return HttpResponse('OK')
