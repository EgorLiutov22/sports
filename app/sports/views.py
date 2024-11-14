from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import datetime
import time


def index(request):
    template = loader.get_template("sports/index.html")
    context = {'title': 'Главная страница',
               'pages': [('football', 'Футбол'),
                         ('basketball', 'Баскетбол'),
                         ('hockey', 'Хоккей'),
                         ('daytime/', 'Время')
                         ]}
    return HttpResponse(template.render(context, request))


def sport(request, sport_name):
    template = loader.get_template("sports/sport.html")
    context = {'title': sport_name,
               'text': f'Новости {sport_name}'
               }
    return HttpResponse(template.render(context, request))

def daytime(request):
    template = loader.get_template("sports/daytime.html")
    if datetime.datetime.now().time().hour <= 6:
        text = 'Доброй ночи'
    elif datetime.datetime.now().time().hour <= 12:
        text = 'Доброе утро'
    elif datetime.datetime.now().time().hour <= 18:
        text = 'Добрый день'
    else:
        text = 'Добрый вечер'
    context = {'title': 'Время',
               'time': time.strftime("%H:%M:%S", time.localtime()),
               'daytime': text
               }
    return HttpResponse(template.render(context, request))
