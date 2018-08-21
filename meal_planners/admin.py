from django.contrib import admin

# Register your models here.

from meal_planners.models import Recipe, Description
admin.site.register(Recipe)
admin.site.register(Description)