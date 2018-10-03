from django.shortcuts import render

from ..views import show_category
from ..forms import PageForm
from ..models import Category

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST': # verifica se a requisição é do tipo POST
        form = PageForm(request.POST)  # requisição é do tipo POST
        if form.is_valid(): # verifica se o form é válido
            if category: # verifica se existe a categoria
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug) # se os dados do formulário estiverem válidos, retorna a página com as páginas de uma categoria
        else:
            print (form.errors) # não salva o formulário se os dados estiverem incorretos
    return render(request, 'rango/add_page.html', {'form': form, 'category': category}) # renderiza o template e passa como contexto o formulário