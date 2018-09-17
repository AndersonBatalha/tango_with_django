from django.shortcuts import render


def about(request):
    context_dict = {'twitter': 'http://twitter.com/tangowithdjango'}

    return render(request, 'rango/about.html', context=context_dict)