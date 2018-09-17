from django.shortcuts import render


def rango_index(request):
    context_dict = {'autor': 'Anderson'}
    return render(request, 'rango/rango_index.html', context=context_dict)