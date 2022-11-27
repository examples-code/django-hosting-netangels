from django.shortcuts import render
from django.http import HttpResponseNotFound

def index(request):
    return render(request, 'home/index.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ошибка 404: Страница не найдена</h1>')
