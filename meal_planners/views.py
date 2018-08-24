from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Recipe, Description
from .forms import RecipeForm, DescriptionForm

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
    # Cannot add several forms on the recipe creation page as all children forms (description, labels...) require a recipe_id that is only assigned after recipe description
    if request.method != 'POST':
        # No data submitted, create a blank form to start creating a new recipe
        form = RecipeForm()
    else:
        # New recipe submitted via POST method, process data
        form = RecipeForm(data=request.POST)
        if form.is_valid():
            new_recipe = form.save()
            return HttpResponseRedirect(reverse('meal_planners:new_recipe_details', args=[new_recipe.pk]))

    context = {'form': form}
    return render (request, 'meal_planners/new_recipe.html', context)

def new_recipe_details(request, recipe_id):
    """Add a new description to a recipe that has just been created"""
    # Can add several forms on the same page: description, labels,... by using form1, form2 and so on as long as we receive recipe_id
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method != 'POST':
        # No data available, create a blank form. 
        form1 = DescriptionForm()
    else:
        # New details submitted via POST method, process data
        form1 = DescriptionForm(data=request.POST)
        if form1.is_valid():
            new_description = form1.save(commit=False)
            new_description.recipe = recipe
            new_description.save()
            return HttpResponseRedirect(reverse('meal_planners:recipe', args=[recipe_id]))

    context = {'recipe': recipe, 'form1': form1}
    return render (request, 'meal_planners/new_recipe_details.html', context)

def edit_recipe(request, recipe_id):
    """Edit an existing recipe"""
    description = Description.objects.get(recipe_id=recipe_id)
    recipe = description.recipe

    if request.method != 'POST':
        # Initial request, view the forms with the current recipe
        form = DescriptionForm(instance = description)

    else:
        # Post data to update the recipe
        form = DescriptionForm(instance = description, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('meal_planners:recipe', args=[recipe_id]))

    context = {'recipe': recipe, 'description': description, 'form': form}
    return render(request, 'meal_planners/edit_recipe.html', context)
