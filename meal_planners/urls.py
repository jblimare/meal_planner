"""Defines URL patterns for meal_planners"""

from django.urls import path
from . import views

app_name = 'meal_planners'

urlpatterns = [
    # Home page
    path('', views.index, name = 'index'),

    # Recipes page
    path('recipes/', views.recipes, name = 'recipes'),

    # Detailed page for each recipe
    path('recipes/<int:recipe_id>/', views.recipe, name = 'recipe'),

    # Page for adding new recipe
    path('recipes/new_recipe/', views.new_recipe, name = 'new_recipe'),

    # Page for adding details of a recipe (description, labels...)
    path('recipes/new_recipe/<int:recipe_id>/', views.new_recipe_details, name = 'new_recipe_details'),

    # Page for editing an existing recipe
    path('recipes/edit_recipe/<int:recipe_id>/', views.edit_recipe, name = 'edit_recipe'),

    # URL to delete recipe
    path('recipes/delete_recipe/<int:recipe_id>/', views.delete_recipe, name = 'delete_recipe')
]

