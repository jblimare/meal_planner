from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Recipe, Description
from .forms import RecipeForm, DescriptionForm
from .recipes_picker import random_recipe
# Create your views here.

def index(request):
    """The home page for Meal Planner"""
    return render(request, 'meal_planners/index.html')

@login_required
def recipes(request):
    """Show all recipes"""
    recipes = Recipe.objects.filter(owner=request.user).order_by('name')
    context = {'recipes' : recipes}
    return render(request, 'meal_planners/recipes.html', context)

@login_required
def recipe(request, recipe_id):
    """Show a single recipe and its description"""
    recipe = Recipe.objects.get(id=recipe_id)

    # Make sure the recipe belongs to the current user
    if recipe.owner != request.user:
        raise Http404

    descriptions = recipe.description_set.all()
    context = {'recipe': recipe, 'descriptions': descriptions}
    return render(request, 'meal_planners/recipe.html', context)

@login_required
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
            new_recipe = form.save(commit=False)
            new_recipe.owner = request.user
            new_recipe.save()
            return HttpResponseRedirect(reverse('meal_planners:new_recipe_details', args=[new_recipe.pk]))

    context = {'form': form}
    return render (request, 'meal_planners/new_recipe.html', context)

@login_required
def new_recipe_details(request, recipe_id):
    """Add a new description to a recipe that has just been created"""
    # Can add several forms on the same page: description, labels,... by using form1, form2 and so on as long as we receive recipe_id
    recipe = Recipe.objects.get(id=recipe_id)

    # Make sure the recipe belongs to the current user
    if recipe.owner != request.user:
        raise Http40

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

@login_required
def edit_recipe(request, recipe_id):
    """Edit an existing recipe"""
    name = Recipe.objects.get(id = recipe_id)
    description = Description.objects.get(recipe_id=recipe_id)
    recipe = description.recipe

    # Make sure the recipe belongs to the current user
    if recipe.owner != request.user:
        raise Http40

    if request.method != 'POST':
        # Initial request, view the forms with the current recipe
        form1 = RecipeForm(instance = name)
        form2 = DescriptionForm(instance = description)

    else:
        # Post data to update the recipe
        form1 = RecipeForm(instance = name, data=request.POST)
        form2 = DescriptionForm(instance = description, data=request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return HttpResponseRedirect(reverse('meal_planners:recipe', args=[recipe_id]))

    context = {'name': name, 'recipe': recipe, 'description': description, 'form1': form1, 'form2': form2}
    return render(request, 'meal_planners/edit_recipe.html', context)

@login_required
def delete_recipe(request, recipe_id):
    """Delete a recipe"""
    if request.method == 'POST':
        name = Recipe.objects.get(id = recipe_id)
        description = Description.objects.get(recipe_id=recipe_id)
        recipe = description.recipe

        description.delete()
        name.delete()
        return HttpResponseRedirect (reverse('meal_planners:recipes'))
       
    context = {'name': name, 'description': description, 'recipe': recipe}
    return render(request, 'meal_planners/recipes.html', context)

@login_required
def get_random_recipe(request):
    """Return a random recipe"""
    days = range(0,7)
    random_recipe()
    
    context = {'random_recipe': random_recipe, 'days': days}
    return render(request, 'meal_planners/recipes_picker.html', context)

