from io import RawIOBase
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Recipe

# Create your views here.

def index(request):

    recipes = Recipe.objects.all()

    menu = {
        'recipes_name': recipes
    }

    return render(request, 'index.html', menu)

def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    recipe_to_show = {
        'recipe':recipe
    }
    return render(request, 'recipe.html', recipe_to_show)
