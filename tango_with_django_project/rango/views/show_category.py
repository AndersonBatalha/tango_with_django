from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View

from ..models import Category, Page

# def show_category(request, category_name_slug): # a função recebe como parâmetro o nome da categoria
#     context_dict = {} # dicionário de contexto a ser passado para o template
#
#     try:
#         category = Category.objects.get(slug=category_name_slug) # busca a categoria pelo nome
#
#         pages = Page.objects.filter(category=category) # busca todas as páginas que pertencem a categoria
#
#         context_dict['pages'] = pages # adiciona o resultado da consulta para o contexto
#         context_dict['category'] = category
#
#     except Category.DoesNotExist: # se a categoria não existe, retorna um valor nulo
#         context_dict['category'] = None
#         context_dict['pages'] = None
#
#     return render(request, 'rango/category.html', context_dict)

class ShowCategory(View):
    context_dict = {} # dicionário de contexto a ser passado para o template
    template = 'rango/category.html'
    category = pages = []

    def get(self, request, category_name_slug):

        try:
            self.category = Category.objects.get(slug=category_name_slug) # busca a categoria pelo nome

            self.pages = Page.objects.filter(category=self.category).order_by('-views') # busca todas as páginas que pertencem a categoria

            self.context_dict['pages'] = self.pages # adiciona o resultado da consulta para o contexto
            self.context_dict['category'] = self.category

        except Category.DoesNotExist: # se a categoria não existe, retorna um valor nulo
            self.context_dict['category'] = None
            self.context_dict['pages'] = None

        self.context_dict['logado'] = request.user.is_authenticated()

        return render(request, self.template, self.context_dict)
