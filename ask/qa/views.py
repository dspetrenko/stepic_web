from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main(request):
    page = request.GET.get('page')

    return HttpResponse('OK\tpage={}'.format(page))


def popular(request):
    page = request.GET.get('page')

    return HttpResponse('OK\tpage={}'.format(page))


def queation(request, id):
    return HttpResponse('OK')
