from django.shortcuts import render

from ..views import index
from ..forms import CategoryForm

def add_category(request):
    form = CategoryForm()
    if request.method == 'POST': # verifica se a requisição é do tipo POST
        form = CategoryForm(request.POST)  # requisição é do tipo POST
        if form.is_valid(): # verifica se o form é válido
            form.save(commit=True) # salva as alterações
            return index(request) # se os dados do formulário estiverem válidos, retorna a página inicial
        else:
            print (form.errors) # não salva o formulário se os dados estiverem incorretos
    return render(request, 'rango/add_category.html', {'form': form}) # renderiza o template e passa como contexto o formulário