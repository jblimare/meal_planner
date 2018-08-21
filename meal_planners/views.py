from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Recipe
from .forms import RecipeForm

# Create your views here.

def index(request):
    """The home page for Meal Planner"""
    return render(request, 'meal_planners/index.html')

def recipes(request):
    """Show all recipes"""
    recipes = Recipe.objects.order_by('name')
    context = {'recipes' : recipes}
    return render(request, 'meal_planners/recipes.html', context)

def recipe(request, recipe_id):
    """Show a single recipe and its description"""
    recipe = Recipe.objects.get(id=recipe_id)
    descriptions = recipe.description_set.all()
    context = {'recipe': recipe, 'descriptions': descriptions}
    return render(request, 'meal_planners/recipe.html', context)

def new_recipe(request):
    """Add a new recipe"""
    if request.method != 'POST':
        # No data submitted, create a blank form to start creating a new recipe
        form = RecipeForm()
    else:
        # New recipe submitted via POST method, process data
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('meal_planners:recipes'))

    context = {'form': form}
    return render (request, 'meal_planners/new_recipe.html', context)