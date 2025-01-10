from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe

from recipes.utils.recipes.factory import make_recipe

def home(request):
    recipes= Recipe.objects.filter(is_published=True).order_by('id')
    return render(request, 'recipes/pages/home.html', context={ 'recipes':recipes })

def category(request, category_id):
    recipe= Recipe.objects.filter(category__id=category_id, is_published=True).order_by('id')
    return render(request, 'recipes/pages/home.html', context={ 'recipes':recipe })

def recipes(request,id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-view.html', context={ 'recipe':recipe})


