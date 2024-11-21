from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import datetime
import time

from .form import UserForm



def index(request):
    template = loader.get_template("sports/index.html")
    context = get_context('Главная страница')
    return HttpResponse(template.render(context, request))


def sport(request, sport_name):
    template = loader.get_template("sports/sport.html")
    d = {'text': f'Новости {sport_name}'}
    context = get_context(sport_name, d)
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

    t = {'time': time.strftime("%H:%M:%S", time.localtime()),
         'daytime': text}
    context = get_context('Время', t)
    return HttpResponse(template.render(context, request))

def user_age(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
    else:
        userform = UserForm()
        content = get_context('Пользователь', {"form": userform})
        return render(request, "user.html", content)


def get_context(title, d=None):
    context = {'title': title,
               'pages': [('football/', 'Футбол'),
                         ('basketball/', 'Баскетбол'),
                         ('hockey/', 'Хоккей'),
                         ('daytime/', 'Время'),
                         ('user_age/', 'Пользователь')
                         ]}
    if d:
        for k in d:
            context[k] = d[k]
    return context

