from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    texto = '''

    <h2>Index do site</h2>

    <br>

    <a href='/rango'>Rango</a><br><br>

    '''
    return HttpResponse(texto)


def rango_index(request):
    texto = '''
    
    <h2>Index do app rango</h2>
    
    <br>
    
    <a href='/'>Voltar</a><br><br>
    <a href='about/'>About</a><br><br>
    
    '''
    return HttpResponse(texto)

def about(request):
    texto = '''

    <h2>Sobre o rango</h2>

    <br>

    <a href='/'>Index</a><br><br>
    <a href='/rango'>Voltar</a><br><br>
    <a href='http://twitter.com/tangowithdjango'>Siga-nos</a><br><br>

    '''

    return HttpResponse(texto)