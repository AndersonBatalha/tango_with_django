from django.shortcuts import render

# Create your views here.
from .models import Category


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    print('Categorias: ', category_list, len(category_list))

    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context=context_dict)


def rango_index(request):
    context_dict = {'autor': 'Anderson'}
    return render(request, 'rango/rango_index.html', context=context_dict)

def about(request):
    context_dict = {'twitter': 'http://twitter.com/tangowithdjango'}

    return render(request, 'rango/about.html', context=context_dict)