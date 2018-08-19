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