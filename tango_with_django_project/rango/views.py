from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Rango says hey there partner!")

def rango_index(request):
    return HttpResponse("Rango app says: 'hey there partner!'")

def about(request):
    return HttpResponse("Rango app says: 'is the about page'")
