from django.shortcuts import render

from ..views import index
from ..forms import CategoryForm

def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)  # requisição é do tipo POST
        if form.is_valid(): # verifica se o form é válido
            form.save(commit=True) # salva as alterações
            return index(request) # retorna a página inicial
        else:
            print (form.errors)
    return render(request, 'rango/add_category.html', {'form': form})