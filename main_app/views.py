from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import datetime




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
