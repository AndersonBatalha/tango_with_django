from rango.models import Category, Page
from django.shortcuts import render


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    print('Categorias: ', category_list, len(category_list))

    pages = Page.objects.order_by('-views')[:5]
    print('Páginas: ', pages, len(pages))

    context_dict = {'categories': category_list, 'pages': pages}
    return render(request, 'rango/index.html', context=context_dict)