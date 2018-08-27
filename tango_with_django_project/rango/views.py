from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    texto = """
    
    <h3>Rango says hey there partner!</h3>

    <br><a href='rango/'>Rango app</a>
    <br><a href='rango/about/'>About</a>
    
    """
    return HttpResponse(texto)

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
