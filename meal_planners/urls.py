"""Defines URL patterns for meal_planners"""

from django.urls import path
from . import views

app_name = 'meal_planners'

urlpatterns = [
    # Home page
    path('', views.index, name = 'index'),

    # Recipes page
    path('recipes/', views.recipes, name = 'recipes'),

]

