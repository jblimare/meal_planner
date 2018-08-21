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
    path('recipe/new_recipe/', views.new_recipe, name = 'new_recipe')
]

