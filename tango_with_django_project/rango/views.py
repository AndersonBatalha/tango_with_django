from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'boldmessage': 'Este texto veio da view'}
    context_dict['autor'] = 'Anderson'
    return render(request, 'rango/index.html', context=context_dict)


def rango_index(request):
    context_dict = {'autor': 'Anderson'}
    return render(request, 'rango/rango_index.html', context=context_dict)

def about(request):
    context_dict = {'twitter': 'http://twitter.com/tangowithdjango'}

    return render(request, 'rango/about.html', context=context_dict)