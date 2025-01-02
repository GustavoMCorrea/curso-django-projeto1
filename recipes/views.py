from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse('Hello, World!')

def about(request):
    return HttpResponse('Sobre')

def contact(request):
    return HttpResponse('Contato')
