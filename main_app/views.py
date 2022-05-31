from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404
import datetime
from .models import Director, Review, Movie
from main_app.forms import LoginForm, RegisterForm


def test(request):
    return HttpResponse('<h1>hw1.4<h1>')


def text1(request):
    dict_ = {
        'title': 'Website1 APPLICATION',
        'text': 'Cайтом заниматеся Эмир из группы python 16-1'
    }
    return render(request, 'proj.html', context=dict_)


def text2(request):
    dict_ = {
        'title': 'Website2 APPLICATION',
        'text': 'Cайт находится в стадий разработки'
    }
    return render(request, 'proj2.html', context=dict_)


def text3(request):
    a = datetime.datetime.today()
    dict_ = {
        'title': 'Website APPLICATION',
        'text': 'Функций сайта будут постоянно обновляться ',
        'time': a
    }
    return render(request, 'proj3.html', context=dict_)


def movie_list_view(request):
    movie_list = Movie.objects.all()
    context = {
        'movie': movie_list
    }
    return render(request, 'FILM_list.html', context=context)


def movie_detail_view(request, id):
    try:
        Movie_detail = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        raise Http404('movie not FOUND!!!')
    return render(request, 'film_detali.html', context={
        'detail': Movie_detail
    })


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
        return render(request, 'login.html', context={
            'form': LoginForm()
        })


def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'register.html', context={
            'form': RegisterForm()
        })
