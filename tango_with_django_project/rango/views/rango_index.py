from django.shortcuts import render
from django.views.generic import View

# def rango_index(request):
#     context_dict = {'autor': 'Anderson'}
#     return render(request, 'rango/rango_index.html', context=context_dict)

class RangoIndex(View):
    context_dict = {}
    template = 'rango/rango_index.html'

    def get(self, request):
        self.context_dict = {'autor': 'Anderson'}
        return render(request, self.template, context=self.context_dict)
