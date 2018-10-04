from django.shortcuts import render
from django.views.generic import View

# def about(request):
#     context_dict = {'twitter': 'http://twitter.com/tangowithdjango'}
#
#     return render(request, 'rango/about.html', context=context_dict)

class About(View):
    context_dict = {}
    template = 'rango/about.html'

    def get(self, request):
        self.context_dict = {'twitter': 'http://twitter.com/tangowithdjango'}

        return render(request, self.template, context=self.context_dict)
