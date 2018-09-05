from .models import Recipe, Description
from .forms import RecipeForm, DescriptionForm
import random

def random_recipe():
    all_recipes = Recipe.objects.all()
    random_recipe = random.choice(all_recipes)
    print(random_recipe)
    return(random_recipe)

