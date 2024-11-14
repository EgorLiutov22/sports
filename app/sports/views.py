from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    template = loader.get_template("sports/index.html")
    context = {'title': 'Главная страница',
               'pages': [('football', 'Футбол'),
                         ('basketball', 'Баскетбол'),
                         ('hockey', 'Хоккей')
                         ]}
    return HttpResponse(template.render(context, request))
