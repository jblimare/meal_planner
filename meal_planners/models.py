from django.db import models

# Create your models here.

class Recipe(models.Model):
    """A recipe that the user can create and view"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name

class Description(models.Model):
    """A description of the recipe"""
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    text = models.TextField(default="Please enter description of your recipe")

    def __str__(self):
        """Return a string representation of the model"""
        return self.text[:50] + "..."