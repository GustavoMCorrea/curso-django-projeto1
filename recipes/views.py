from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe

from recipes.utils.recipes.factory import make_recipe

def home(request):
    recipes= Recipe.objects.filter(is_published=True).order_by('id')
    return render(request, 'recipes/pages/home.html', context={ 'recipes':recipes })

def category(request, category_id):
    try:
        recipe = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('id')
        if not recipe.exists():
            raise Recipe.DoesNotExist
        return render(request, 'recipes/pages/category.html', context={ 'recipes':recipe , 'title': f'{recipe.first().category.name} - Category'})
    except Recipe.DoesNotExist:
        return HttpResponse('Categoria não encontrada', status=404)

    

def recipes(request,id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-view.html', context={ 'recipe':recipe})


