from django.db import models

# Create your models here.

class Recipe(models.Model):
    """A recipe that the user can create and view"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default="Please enter description of your recipe")

    def __str__(self):
        """Return a string representationof the model"""
        return self.name

