from django.shortcuts import render
from .models import Recipe

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
    context = {'recipe': recipe}
    return render(request, 'meal_planners/recipe.html', context)