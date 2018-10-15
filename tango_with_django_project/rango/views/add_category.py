from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from ..forms import CategoryForm

# def add_category(request):
#     form = CategoryForm()
#     if request.method == 'POST': # verifica se a requisição é do tipo POST
#         form = CategoryForm(request.POST)  # requisição é do tipo POST
#         if form.is_valid(): # verifica se o form é válido
#             form.save(commit=True) # salva as alterações
#             return index(request) # se os dados do formulário estiverem válidos, retorna a página inicial
#         else:
#             print (form.errors) # não salva o formulário se os dados estiverem incorretos
#     return render(request, 'rango/add_category.html', {'form': form}) # renderiza o template e passa como contexto o formulário

class AddCategory(View):
    form_class = CategoryForm
    initial = {}
    template = 'rango/add_category.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('index'))

        return render(request, self.template, {'form': form})