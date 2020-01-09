from django import forms
from .models import Category


class TodoForm(forms.Form):

    categories = Category.objects.all()
    choices = []
    for category in categories:
        choices.append((category.name, category.name))

    description = forms.CharField(label="description")
    category = forms.ChoiceField(choices=choices)
    date = forms.TimeField(label="Due Date", widget=forms.TextInput(
        attrs={'type': 'date'}
    ))
