from django.shortcuts import render
from ..models import Category, Page


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