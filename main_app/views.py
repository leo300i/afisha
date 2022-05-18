from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
import datetime
from .models import Director, Review, Movie


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
