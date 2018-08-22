from django import forms

from .models import Recipe, Description

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']
        labels = {'name':''}

class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = ['text']
        labels = {'text': ''}
