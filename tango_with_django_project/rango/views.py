from django.shortcuts import render

# Create your views here.
from .models import Category, Page


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

def show_category(request, category_name_slug): # a função recebe como parâmetro o nome da categoria
    context_dict = {} # dicionário de contexto a ser passado para o template

    try:
        category = Category.objects.get(slug=category_name_slug) # busca a categoria pelo nome

        pages = Page.objects.filter(category=category) # busca todas as páginas que pertencem a categoria

        context_dict['pages'] = pages # adiciona o resultado da consulta para o contexto
        context_dict['category'] = category

    except Category.DoesNotExist: # se a categoria não existe, retorna um valor nulo
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)

