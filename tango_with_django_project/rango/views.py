from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Index do site")

def rango_index(request):
    return HttpResponse("Index do app rango")