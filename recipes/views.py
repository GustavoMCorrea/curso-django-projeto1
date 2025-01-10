from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Recipe

from recipes.utils.recipes.factory import make_recipe

def home(request):
    recipes= Recipe.objects.filter(is_published=True).order_by('id')
    return render(request, 'recipes/pages/home.html', context={ 'recipes':recipes })

def category(request, category_id):
    try:
        recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True).order_by('id'))
        title = f'{recipes[0].category.name} - Category'
    except Http404:
        return HttpResponse('Categoria não encontrada', status=404)
    return render(request, 'recipes/pages/category.html', context={ 'recipes': recipes, 'title': title })

    
def recipes(request,id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-view.html', context={ 'recipe':recipe})


