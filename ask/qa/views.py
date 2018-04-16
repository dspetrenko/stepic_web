from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.core.paginator import Paginator

from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User

from django.urls import reverse

from .models import Question as Q
from .models import Answer as A

from .forms import AskForm, AnswerForm

from .forms import Signupform
from .forms import LoginForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user=user)

            return HttpResponseRedirect(reverse(main))
    else:
        form = Signupform()

    return render(request, 'signup.html', context={'form': form})


def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse(main))

            else:
                form.add_error('', "Your username and password didn't match. Please try again.")

    else:
        form = LoginForm()

    return render(request, 'login.html', context={'form': form})


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

    if request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            from django.contrib.auth.models import User

            if request.user.is_authenticated:
                answer.author = request.user
            else:
                answer.author = User.objects.get(id=1)

            answer.save()
            return HttpResponseRedirect(answer.question.get_absolute_url())

    else:
        form = AnswerForm()

    context = {
        'question': q,
        'form': form,
        'answers': A.objects.filter(question=q)
    }
    return render(request, 'question.html', context=context)


def ask(request):

    if request.method == 'POST':
        form = AskForm(request.POST)

        if form.is_valid():
            new_question = form.save(commit=False)

            from django.contrib.auth.models import User

            new_question.author = User.objects.get(id=1)
            new_question.save()

            return HttpResponseRedirect(new_question.get_absolute_url())

    else:
        form = AskForm()

    context = {
        'form': form,
    }

    return render(request, 'ask.html', context=context)
