from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'boldmessage': 'Este texto veio da view'}
    return render(request, 'rango/index.html', context=context_dict)

def rango_index(request):
    texto = """

    <h3>Rango app says: 'hey there partner!'</h3>

    <br><br><a href='about/'>About</a>
    <br><br><a href='/'>Voltar</a>


    """

    return HttpResponse(texto)

def about(request):
    texto = """

    <h3>Rango app says: 'is the about page'</h3>

    <br><br><a href='/'>Index</a>
    <br><br><a href='/rango'>Voltar</a>


    """
    return HttpResponse(texto)
