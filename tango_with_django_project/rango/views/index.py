from django.views.generic import View
from ..models import Category, Page
from django.shortcuts import render


# def index(request):
#     category_list = Category.objects.order_by('-likes')[:5]
#     print('Categorias: ', category_list, len(category_list))
#
#     pages = Page.objects.order_by('-views')[:5]
#     print('Páginas: ', pages, len(pages))
#
#     context_dict = {'categories': category_list, 'pages': pages}
#     return render(request, 'rango/index.html', context=context_dict)

class Index(View):
    context_dict = category_list = pages = {}
    template = 'rango/index.html'

    def get(self, request):
        self.category_list = Category.objects.order_by('-likes')[:5]
        print('Categorias: ', self.category_list, len(self.category_list))

        self.pages = Page.objects.order_by('-views')[:5]
        print('Páginas: ', self.pages, len(self.pages))

        self.context_dict = {'categories': self.category_list, 'pages': self.pages}
        return render(request, self.template, context=self.context_dict)