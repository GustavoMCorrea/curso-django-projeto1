from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/pages/home.html')

def recipes(request):
    return render(request, 'recipes/pages/recipe-view.html')


